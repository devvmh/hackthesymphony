#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py collectstatic
chgrp -R www-data static
chmod u=rw,g=r,o= -R static
