#!/usr/bin/env bash
# Instala el proyecto en un VPS de Hostinger con Ubuntu 24.04 (plantilla limpia, sin panel).
# Monta nginx + gunicorn + systemd, HTTPS con Let's Encrypt, cortafuegos y copias de seguridad diarias.
#
# Uso (como root):
#   bash instalar_vps.sh midominio.com tu@correo.com [rama]
#   bash instalar_vps.sh                      # sin dominio: la web queda accesible por la IP, sin HTTPS
#
# Se puede volver a ejecutar sin perder datos: conserva .env, la base de datos y los archivos subidos.
set -euo pipefail

DOMINIO="${1:-}"
EMAIL="${2:-}"
RAMA="${3:-main}"
REPO="${REPO:-https://github.com/NikiDevelop/Django-Blog.git}"
APP_DIR="${APP_DIR:-/srv/django-blog}"
APP_USER="${APP_USER:-django}"
SERVICIO="django-blog"
SOCKET="/run/$SERVICIO/gunicorn.sock"
BACKUPS="/var/backups/django-blog"

paso() { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }
aviso() { printf '\033[1;33m[!] %s\033[0m\n' "$*"; }
como_app() { sudo -u "$APP_USER" -H "$@"; }
manage() { como_app "$APP_DIR/venv/bin/python" "$APP_DIR/manage.py" "$@"; }

ip_servidor() { hostname -I | awk '{print $1}'; }

# Nombres de dominio que se van a servir: el dominio y, si es un dominio raíz, también www.
nombres_dominio() {
    [[ -z "$DOMINIO" ]] && return
    echo "$DOMINIO"
    if [[ "$DOMINIO" != www.* && "$(tr -cd '.' <<<"$DOMINIO" | wc -c)" -eq 1 ]]; then
        echo "www.$DOMINIO"
    fi
}

instalar_paquetes() {
    paso "Instalando paquetes del sistema"
    export DEBIAN_FRONTEND=noninteractive
    apt-get update -q
    apt-get install -y -q python3-venv python3-dev build-essential git nginx sqlite3 \
        certbot python3-certbot-nginx ufw curl
}

preparar_usuario() {
    paso "Preparando el usuario $APP_USER"
    id -u "$APP_USER" >/dev/null 2>&1 || useradd --system --create-home --shell /usr/sbin/nologin "$APP_USER"
    install -d -o "$APP_USER" -g "$APP_USER" -m 755 "$APP_DIR"
    install -d -o "$APP_USER" -g "$APP_USER" -m 750 "$BACKUPS"
}

descargar_codigo() {
    paso "Descargando el código (rama $RAMA)"
    if [[ -d "$APP_DIR/.git" ]]; then
        como_app git -C "$APP_DIR" fetch --quiet origin "$RAMA"
        como_app git -C "$APP_DIR" checkout --quiet -B "$RAMA" "origin/$RAMA"
    else
        como_app git clone --quiet --branch "$RAMA" "$REPO" "$APP_DIR"
    fi
}

instalar_python() {
    paso "Instalando dependencias de Python"
    [[ -x "$APP_DIR/venv/bin/python" ]] || como_app python3 -m venv "$APP_DIR/venv"
    como_app "$APP_DIR/venv/bin/pip" install --quiet --upgrade pip
    como_app "$APP_DIR/venv/bin/pip" install --quiet -r "$APP_DIR/requirements.txt"
}

crear_env() {
    if [[ -f "$APP_DIR/.env" ]]; then
        paso "Conservando el .env existente"
        return
    fi
    paso "Creando .env con una clave secreta nueva"
    local hosts origenes nombre
    hosts="$(ip_servidor),localhost,127.0.0.1"
    origenes=""
    while read -r nombre; do
        [[ -z "$nombre" ]] && continue
        hosts="$nombre,$hosts"
        origenes="${origenes:+$origenes,}https://$nombre"
    done < <(nombres_dominio)

    umask 077
    cat > "$APP_DIR/.env" <<EOF
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')
DJANGO_ALLOWED_HOSTS=$hosts
DJANGO_CSRF_TRUSTED_ORIGINS=$origenes
DJANGO_HTTPS=False
DJANGO_HSTS_SECONDS=0
EOF
    umask 022
    chown "$APP_USER:$APP_USER" "$APP_DIR/.env"
    chmod 600 "$APP_DIR/.env"
}

preparar_django() {
    paso "Aplicando migraciones y reuniendo estáticos"
    manage migrate --noinput
    manage collectstatic --noinput --verbosity 0
    chmod 640 "$APP_DIR/db.sqlite3"
    # El contenido inicial se carga solo la primera vez: después se edita desde el admin
    if [[ ! -f "$APP_DIR/.contenido_cargado" ]]; then
        paso "Cargando las 5 webs"
        manage cargar_nichos
        como_app touch "$APP_DIR/.contenido_cargado"
    fi
}

configurar_gunicorn() {
    paso "Configurando el servicio $SERVICIO (gunicorn)"
    cat > "/etc/systemd/system/$SERVICIO.service" <<EOF
[Unit]
Description=Django Blog y webs de tendencias (gunicorn)
After=network.target

[Service]
User=$APP_USER
Group=www-data
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/gunicorn core.wsgi:application --workers 3 --timeout 60 --bind unix:$SOCKET --umask 007 --access-logfile - --error-logfile -
RuntimeDirectory=$SERVICIO
Restart=always
RestartSec=3
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full
ProtectHome=true

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
    systemctl enable --quiet "$SERVICIO"
    systemctl restart "$SERVICIO"
}

configurar_nginx() {
    paso "Configurando nginx"
    local nombres
    nombres="$(nombres_dominio | tr '\n' ' ')"
    nombres="${nombres:-_}"
    # Si certbot ya añadió HTTPS en una ejecución anterior, no se sobrescribe su configuración
    if [[ -f "/etc/nginx/sites-available/$SERVICIO" ]] && grep -q "managed by Certbot" "/etc/nginx/sites-available/$SERVICIO"; then
        aviso "nginx ya tiene HTTPS configurado por certbot: se conserva"
    else
        cat > "/etc/nginx/sites-available/$SERVICIO" <<'EOF'
server {
    listen 80;
    listen [::]:80;
    server_name __NOMBRES__;

    client_max_body_size 20M;

    gzip on;
    gzip_types text/plain text/css application/javascript application/json application/xml image/svg+xml;

    # La portada del dominio muestra las 5 webs de tendencias
    location = / {
        return 302 /webs/;
    }

    location /static/ {
        alias __APP_DIR__/staticfiles/;
        expires 7d;
        access_log off;
    }

    location /media/ {
        alias __APP_DIR__/media/;
        expires 7d;
    }

    location / {
        proxy_pass http://unix:__SOCKET__;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
    }
}
EOF
        sed -i "s|__NOMBRES__|$nombres|; s|__APP_DIR__|$APP_DIR|g; s|__SOCKET__|$SOCKET|" "/etc/nginx/sites-available/$SERVICIO"
    fi
    ln -sf "/etc/nginx/sites-available/$SERVICIO" "/etc/nginx/sites-enabled/$SERVICIO"
    rm -f /etc/nginx/sites-enabled/default
    nginx -t
    systemctl reload nginx || systemctl restart nginx
}

configurar_cortafuegos() {
    paso "Configurando el cortafuegos"
    local puerto_ssh
    # Abrimos el puerto SSH real antes de activar ufw para no quedarnos fuera
    puerto_ssh="$(sshd -T 2>/dev/null | awk '$1 == "port" {print $2; exit}')"
    ufw allow "${puerto_ssh:-22}/tcp" >/dev/null
    ufw allow 'Nginx Full' >/dev/null
    ufw --force enable >/dev/null
    ufw status | sed 's/^/    /'
}

configurar_backups() {
    paso "Programando copias de seguridad diarias (03:30, se conservan 14 días)"
    chmod +x "$APP_DIR/deploy/backup.sh"
    cat > "/etc/cron.d/$SERVICIO-backup" <<EOF
30 3 * * * $APP_USER APP_DIR=$APP_DIR DESTINO=$BACKUPS $APP_DIR/deploy/backup.sh >> $BACKUPS/backup.log 2>&1
EOF
}

activar_https() {
    if [[ -z "$DOMINIO" || -z "$EMAIL" ]]; then
        aviso "Sin dominio y correo no se puede activar HTTPS. Vuelve a ejecutar el script con ambos cuando tengas dominio."
        return
    fi
    paso "Activando HTTPS con Let's Encrypt"
    local ip nombre args=()
    ip="$(ip_servidor)"
    while read -r nombre; do
        if getent ahostsv4 "$nombre" | awk '{print $1}' | grep -qx "$ip"; then
            args+=(-d "$nombre")
        else
            aviso "$nombre todavía no apunta a $ip: revisa los registros DNS en Hostinger"
        fi
    done < <(nombres_dominio)

    if [[ ${#args[@]} -eq 0 ]]; then
        aviso "El DNS aún no apunta a este servidor. Cuando se propague, vuelve a ejecutar este script."
        return
    fi
    if certbot --nginx --non-interactive --agree-tos --redirect -m "$EMAIL" "${args[@]}"; then
        sed -i 's/^DJANGO_HTTPS=.*/DJANGO_HTTPS=True/' "$APP_DIR/.env"
        systemctl restart "$SERVICIO"
    else
        aviso "certbot no pudo emitir el certificado. La web sigue funcionando por HTTP."
    fi
}

comprobar() {
    paso "Comprobando que la web responde"
    local respuesta=""
    for _ in 1 2 3 4 5 6 7 8 9 10; do
        respuesta="$(curl -fsS --unix-socket "$SOCKET" -H 'X-Forwarded-Proto: https' http://localhost/salud/ 2>/dev/null || true)"
        [[ "$respuesta" == "ok" ]] && break
        sleep 1
    done
    if [[ "$respuesta" != "ok" ]]; then
        aviso "La web no responde. Revisa los registros con: journalctl -u $SERVICIO -n 50"
        exit 1
    fi
    echo "    /salud/ responde ok"
}

resumen() {
    local url
    url="http://$(ip_servidor)"
    [[ -n "$DOMINIO" ]] && url="http://$DOMINIO"
    grep -q '^DJANGO_HTTPS=True' "$APP_DIR/.env" && url="https://$DOMINIO"
    paso "Instalación terminada"
    cat <<EOF
    Webs:   $url/webs/
    Admin:  $url/admin/

    Crea tu usuario administrador con:
      sudo -u $APP_USER $APP_DIR/venv/bin/python $APP_DIR/manage.py createsuperuser

    Actualizar tras cambios en GitHub:  sudo bash $APP_DIR/deploy/actualizar.sh
    Ver registros:                      journalctl -u $SERVICIO -f
    Copias de seguridad:                $BACKUPS
EOF
}

main() {
    [[ $EUID -eq 0 ]] || { echo "Ejecuta este script como root (sudo bash $0 ...)"; exit 1; }
    instalar_paquetes
    preparar_usuario
    descargar_codigo
    instalar_python
    crear_env
    preparar_django
    configurar_gunicorn
    configurar_nginx
    configurar_cortafuegos
    configurar_backups
    comprobar
    activar_https
    resumen
}

# Ejecutar solo cuando se llama directamente (permite cargar las funciones en pruebas)
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    main "$@"
fi
