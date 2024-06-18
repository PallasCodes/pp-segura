#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=server.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=server.settings
python manage.py migrate --settings=server.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=server.settings server.wsgi:application --bind 0.0.0.0:$PORT