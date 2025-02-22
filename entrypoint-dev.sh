#!/bin/bash

python move_hooks.py

python manage.py migrate
python3 manage.py load_data 

# service cron start
# python manage.py crontab add

python manage.py runserver 0.0.0.0:8000