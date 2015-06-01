#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py dumpdata appcode.Question appcode.Answer appcode.Concert > appcode/fixtures/initial_data.json
