#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'devin@callysto.com', 'password')" | python manage.py shell
