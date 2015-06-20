#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py collectstatic
chgrp -R www-data static
find static -type d -exec chmod u=rwx,g=rx,o= '{}' \;
find static -type f -exec chmod u=rw,g=r,o= '{}' \;
