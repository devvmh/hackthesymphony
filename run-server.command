#!/bin/bash

echo
SCRIPT=$(basename $0)
cd $(find ~ SCRIPT)
python manage.py runserver
read -p "Press Enter to close this window" FOOBAR
