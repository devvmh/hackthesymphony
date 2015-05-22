#!/bin/bash

echo
cd $(dirname $0)
python manage.py syncdb

read -p "Press Enter to close this window" FOOBAR
