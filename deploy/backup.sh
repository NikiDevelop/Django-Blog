#!/usr/bin/env bash
# Copia de seguridad de la base de datos y de los archivos subidos.
# La ejecuta cada noche el cron que instala instalar_vps.sh, y actualizar.sh antes de cada actualización.
set -euo pipefail

APP_DIR="${APP_DIR:-/srv/django-blog}"
DESTINO="${DESTINO:-/var/backups/django-blog}"
DIAS="${DIAS:-14}"
FECHA="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$DESTINO"

if [[ -f "$APP_DIR/db.sqlite3" ]]; then
    # .backup hace una copia consistente aunque la web esté escribiendo en ese momento
    sqlite3 "$APP_DIR/db.sqlite3" ".backup '$DESTINO/db-$FECHA.sqlite3'"
    gzip "$DESTINO/db-$FECHA.sqlite3"
fi

if [[ -d "$APP_DIR/media" ]]; then
    tar -czf "$DESTINO/media-$FECHA.tar.gz" -C "$APP_DIR" media
fi

find "$DESTINO" -type f -mtime +"$DIAS" -delete
echo "Copia creada en $DESTINO ($FECHA)"
