#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python manage.py dumpdata appcode.Concert

read -p "Press Enter to close this window" FOOBAR
