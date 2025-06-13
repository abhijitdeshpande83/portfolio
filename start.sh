#!/bin/bash
python manage.py migrate

cron
# log that cron started
echo "[start.sh] Cron started at $(date)"

exec gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000