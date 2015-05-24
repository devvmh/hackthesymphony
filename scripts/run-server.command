#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python manage.py runserver

read -p "Press Enter to close this window" FOOBAR
