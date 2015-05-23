#!/bin/bash

echo
cd $(dirname "$0")
sudo -H pip install -r requirements.txt

read -p "Press Enter to close this window" FOOBAR
