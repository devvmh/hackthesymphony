#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py syncdb
python manage.py loaddata appcode/fixtures/fixtures.json
