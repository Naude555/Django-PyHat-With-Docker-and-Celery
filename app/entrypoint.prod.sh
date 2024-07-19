#!/bin/sh

# ADD HERE
python manage.py collectstatic --noinput

exec "$@"
