#!/bin/bash

echo
cd $(basename "$0")
python manage.py syncdb

read -p "Press Enter to close this window" FOOBAR
