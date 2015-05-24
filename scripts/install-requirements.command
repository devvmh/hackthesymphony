#!/bin/bash

echo
cd $(basename "$0")
sudo -H easy_install pip
sudo -H pip install -r requirements.txt

read -p "Press Enter to close this window" FOOBAR
