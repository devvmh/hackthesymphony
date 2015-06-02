#!/bin/bash

echo
cd $(dirname "$0")/..
if [ -f "db.sqlite3" ]; then
  echo "Warning: there is already a database file at db.sqlite3."
  read -p "Press Enter to delete it and continue, Ctrl+C to abort" FOOBAR
  rm db.sqlite3
fi
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'devin@callysto.com', 'password')" | python manage.py shell
scripts/load-fixtures.command
