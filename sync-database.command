#!/bin/bash

echo
SCRIPT=$(basename $0)
cd $(find ~ SCRIPT)
python manage.py syncdb

read -p "Press Enter to close this window" FOOBAR
