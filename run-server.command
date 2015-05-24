#!/bin/bash

echo
cd $(dirname "$0")
pwd
python manage.py runserver
read -p "Press Enter to close this window" FOOBAR
