#!/bin/sh

cd /code
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000