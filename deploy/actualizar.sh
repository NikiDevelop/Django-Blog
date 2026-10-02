#!/usr/bin/env bash
# Actualiza el código del VPS con lo último de GitHub y reinicia la web.
# Hace una copia de seguridad antes y, si la web no responde después, vuelve a la versión anterior.
#
# Uso (como root):  bash /srv/django-blog/deploy/actualizar.sh [rama]
set -euo pipefail

APP_DIR="${APP_DIR:-/srv/django-blog}"
APP_USER="${APP_USER:-django}"
SERVICIO="django-blog"
SOCKET="/run/$SERVICIO/gunicorn.sock"
BACKUPS="/var/backups/django-blog"

paso() { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }
como_app() { sudo -u "$APP_USER" -H "$@"; }
manage() { como_app "$APP_DIR/venv/bin/python" "$APP_DIR/manage.py" "$@"; }

# Encadenado con && para que cualquier fallo llegue a main() y se pueda volver atrás
desplegar_version() {
    como_app git -C "$APP_DIR" checkout --quiet -B "$1" "$2" &&
        como_app "$APP_DIR/venv/bin/pip" install --quiet -r "$APP_DIR/requirements.txt" &&
        manage migrate --noinput &&
        manage collectstatic --noinput --verbosity 0 &&
        systemctl restart "$SERVICIO"
}

responde() {
    local respuesta=""
    for _ in 1 2 3 4 5 6 7 8 9 10; do
        respuesta="$(curl -fsS --unix-socket "$SOCKET" -H 'X-Forwarded-Proto: https' http://localhost/salud/ 2>/dev/null || true)"
        [[ "$respuesta" == "ok" ]] && return 0
        sleep 1
    done
    return 1
}

main() {
    [[ $EUID -eq 0 ]] || { echo "Ejecuta este script como root (sudo bash $0)"; exit 1; }
    local rama anterior
    rama="${1:-$(como_app git -C "$APP_DIR" rev-parse --abbrev-ref HEAD)}"
    anterior="$(como_app git -C "$APP_DIR" rev-parse HEAD)"

    paso "Copia de seguridad previa"
    como_app env APP_DIR="$APP_DIR" DESTINO="$BACKUPS" bash "$APP_DIR/deploy/backup.sh"

    paso "Descargando la rama $rama"
    como_app git -C "$APP_DIR" fetch --quiet origin "$rama"
    if [[ "$(como_app git -C "$APP_DIR" rev-parse "origin/$rama")" == "$anterior" ]]; then
        echo "    Ya estás en la última versión."
        exit 0
    fi

    paso "Instalando la nueva versión"
    if desplegar_version "$rama" "origin/$rama" && responde; then
        paso "Actualización completada: $(como_app git -C "$APP_DIR" log -1 --format='%h %s')"
    else
        paso "La actualización ha fallado: volviendo a la versión anterior (${anterior:0:7})"
        desplegar_version "$rama" "$anterior" || true
        if responde; then
            echo "    La web vuelve a funcionar con la versión anterior."
        else
            echo "    ¡Atención! La web sigue sin responder."
        fi
        echo "    Revisa los registros con: journalctl -u $SERVICIO -n 50"
        echo "    Si la base de datos quedó dañada, restaura la última copia de $BACKUPS"
        exit 1
    fi
}

# Todo el script vive en main(): bash lo lee entero antes de que git cambie este mismo fichero
main "$@"
