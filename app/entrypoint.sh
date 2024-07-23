#!/bin/sh

# python manage.py flush --no-input
# python manage.py makemigrations
python manage.py migrate
python manage.py tailwind build
python manage.py collectstatic --noinput

exec "$@"
