#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'devin@callysto.com', 'password')" | python manage.py shell

read -p "Press Enter to close this window" FOOBAR
