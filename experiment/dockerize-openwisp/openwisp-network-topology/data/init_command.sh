#!/bin/sh
python manage.py migrate --noinput
python load_init_data.py
python manage.py runserver 0.0.0.0:8001
