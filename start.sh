#!/bin/bash
python manage.py migrate

exec gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000