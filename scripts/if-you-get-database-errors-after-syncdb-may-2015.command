lol
#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py migrate --fake appcode 0001_initial
python manage.py syncdb
