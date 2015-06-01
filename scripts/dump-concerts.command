#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py dumpdata appcode.Concert | sed -e 's/^\[//' -e 's/\]$//' > scripts/concert-fixtures.json
