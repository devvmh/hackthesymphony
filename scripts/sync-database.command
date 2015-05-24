#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python manage.py syncdb

read -p "Press Enter to close this window" FOOBAR
