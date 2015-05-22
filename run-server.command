#!/bin/bash

echo
cd $(dirname $0)
python manage.py runserver
