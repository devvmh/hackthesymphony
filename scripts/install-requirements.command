#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
sudo -H easy_install pip
sudo -H pip install -r requirements.txt

read -p "Press Enter to close this window" FOOBAR
