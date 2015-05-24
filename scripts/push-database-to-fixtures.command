#!/bin/bash

echo
c{d $(dirname "$0")/..
python manage.py dumpdata appcode.Question appcode.Answer appcode.Concert > appcode/fixtures/initial_data.json

read -p "Press Enter to close this window" FOOBAR
