# Publicar en Hostinger

Guía para poner en internet el blog y las 5 webs de tendencias en un VPS de Hostinger.

## 1. Qué plan necesitas

Django necesita un proceso de Python siempre encendido. En Hostinger eso solo es posible en un **VPS**: los planes
de hosting web compartido y Cloud no ejecutan aplicaciones Python.

- **VPS KVM 1** (1 vCPU, 4 GB de RAM) es suficiente para empezar.
- Sistema operativo: **Ubuntu 24.04** (la plantilla limpia, sin panel). No elijas la plantilla «Django» con
  OpenLiteSpeed: el script instala su propio servidor web (nginx) y chocarían.

## 2. Apunta tu dominio al VPS

En hPanel → **Dominios** → tu dominio → **DNS / Nameservers**, crea o edita estos registros con la IP de tu VPS
(la ves en hPanel → VPS → Visión general):

| Tipo | Nombre | Apunta a |
|------|--------|----------|
| A | `@` | IP del VPS |
| A | `www` | IP del VPS |

El cambio puede tardar desde unos minutos hasta unas horas. Si el dominio no es de Hostinger, haz lo mismo en el
panel DNS de tu proveedor.

## 3. Abre el terminal del VPS

En hPanel → VPS → **Terminal del navegador**, o desde tu ordenador:

```
ssh root@IP_DEL_VPS
```

## 4. Instala todo con un comando

Cambia `midominio.com` y el correo por los tuyos. El correo solo se usa para avisos de Let's Encrypt sobre el
certificado HTTPS.

```
curl -fsSLo instalar.sh https://raw.githubusercontent.com/NikiDevelop/Django-Blog/main/deploy/instalar_vps.sh
bash instalar.sh midominio.com tu@correo.com main
```

> Mientras el código nuevo no esté unido a `main`, usa la rama de trabajo:
>
> ```
> curl -fsSLo instalar.sh https://raw.githubusercontent.com/NikiDevelop/Django-Blog/refs/heads/claude/trending-websites-creation-q64tw6/deploy/instalar_vps.sh
> bash instalar.sh midominio.com tu@correo.com claude/trending-websites-creation-q64tw6
> ```

Tarda unos minutos. El script:

1. Instala Python, nginx, certbot, el cortafuegos y SQLite.
2. Descarga el código en `/srv/django-blog` y lo ejecuta con un usuario sin privilegios (`django`).
3. Crea `/srv/django-blog/.env` con una clave secreta aleatoria y `DEBUG` desactivado.
4. Aplica las migraciones, reúne los estáticos y carga las 5 webs (solo la primera vez).
5. Arranca gunicorn como servicio del sistema (`django-blog`), que se reinicia solo si falla.
6. Configura nginx: estáticos con caché, compresión y la raíz del dominio redirigida a `/webs/`.
7. Activa el cortafuegos dejando abiertos SSH, HTTP y HTTPS.
8. Programa una copia de seguridad diaria a las 03:30 (se guardan 14 días).
9. Comprueba que la web responde y, si el DNS ya apunta al VPS, activa HTTPS con renovación automática.

Si el DNS todavía no estaba listo, la web funcionará por HTTP. Cuando se propague, **vuelve a ejecutar el mismo
comando**: no borra nada y solo añadirá el certificado.

## 5. Crea tu usuario administrador

```
sudo -u django /srv/django-blog/venv/bin/python /srv/django-blog/manage.py createsuperuser
```

Entra en `https://midominio.com/admin/` para editar artículos, comparativas, tendencias y productos. Lo primero:
añade tus **enlaces de afiliado** en cada producto.

## Día a día

| Tarea | Comando |
|-------|---------|
| Publicar cambios subidos a GitHub | `bash /srv/django-blog/deploy/actualizar.sh` |
| Ver registros en directo | `journalctl -u django-blog -f` |
| Reiniciar la web | `systemctl restart django-blog` |
| Copia de seguridad manual | `sudo -u django bash /srv/django-blog/deploy/backup.sh` |

`actualizar.sh` hace una copia de seguridad, descarga la última versión, aplica migraciones y reinicia. Si algo
falla o la web deja de responder, **vuelve sola a la versión anterior**.

### Restaurar una copia de seguridad

Las copias están en `/var/backups/django-blog` (`db-FECHA.sqlite3.gz` y `media-FECHA.tar.gz`):

```
systemctl stop django-blog
gunzip -c /var/backups/django-blog/db-FECHA.sqlite3.gz > /srv/django-blog/db.sqlite3
chown django:django /srv/django-blog/db.sqlite3 && chmod 640 /srv/django-blog/db.sqlite3
systemctl start django-blog
```

Las copias viven en el mismo VPS. Descarga una de vez en cuando a tu ordenador y revisa en hPanel las copias de
seguridad del propio VPS.

### No vuelvas a ejecutar `cargar_nichos` en producción

Ese comando restablece el contenido original de las webs y **sobrescribe lo que hayas editado en el admin** en esos
mismos artículos y productos. El instalador lo ejecuta una sola vez.

## Después de publicar

### Seguridad

- [ ] Accede por SSH con clave en lugar de contraseña (hPanel → VPS → Claves SSH).
- [ ] Usa una contraseña larga y única para el admin.
- [ ] Cuando HTTPS funcione bien unos días, activa HSTS: en `/srv/django-blog/.env` pon
      `DJANGO_HSTS_SECONDS=3600`, reinicia con `systemctl restart django-blog` y, si todo va bien, súbelo a
      `31536000`.
- [ ] Ubuntu suele traer activadas las actualizaciones automáticas de seguridad (`unattended-upgrades`). Revisa de
      vez en cuando lo pendiente con `apt list --upgradable`.

### SEO

- [ ] Da de alta el dominio en Google Search Console y envía `https://midominio.com/sitemap.xml`.
- [ ] Comprueba `https://midominio.com/robots.txt`.
- [ ] Revisa algunas páginas con la herramienta de inspección de URL de Search Console.

### Monitorización

- [ ] Crea un monitor gratuito (UptimeRobot, Better Stack…) que consulte `https://midominio.com/salud/` cada
      5 minutos: responde `ok` si Django y la base de datos funcionan.
- [ ] Mira el uso de CPU, memoria y disco en hPanel → VPS.

## Riesgos y cómo se cubren

| Riesgo | Señal | Respuesta |
|--------|-------|-----------|
| El DNS no apunta aún al VPS | El script avisa y no emite el certificado | Esperar y repetir el comando de instalación |
| Una actualización rompe la web | `actualizar.sh` detecta que `/salud/` no responde | Vuelta atrás automática; restaurar copia si hiciera falta |
| Pérdida de datos | — | Copia diaria en el VPS + copias del VPS en hPanel + descargas propias |
| Caduca el certificado | Correo de Let's Encrypt | Se renueva solo (`certbot.timer`); comprobar con `certbot renew --dry-run` |
| Mucho tráfico con escrituras | Lentitud en el admin | SQLite va bien para un blog; si crece mucho, migrar a PostgreSQL |

## Próximos pasos recomendados

1. **Analítica con consentimiento**: GA4 con un banner de cookies (CMP) y el modo de consentimiento de Google.
   Es imprescindible antes de usar AdSense.
2. **Un dominio por web**: ahora las 5 webs viven en `midominio.com/webs/<web>/`. Si compras un dominio para cada
   una, se puede hacer que cada dominio muestre directamente su web.
3. **Doble factor (MFA) en el admin**.
4. **CDN** (por ejemplo, Cloudflare) si el tráfico crece.
