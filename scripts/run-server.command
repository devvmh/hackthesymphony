#!/bin/bash

echo
cd $(basename "$0")
python manage.py runserver

read -p "Press Enter to close this window" FOOBAR
