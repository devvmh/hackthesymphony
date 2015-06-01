#!/bin/bash

echo
cd $(dirname "$0")/..
sudo -H easy_install pip
sudo -H pip install -r requirements.txt
