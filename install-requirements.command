#!/bin/bash

echo
SCRIPT=$(basename $0)
cd $(find ~ SCRIPT)
pip install -r requirements.txt

read -p "Press Enter to close this window" FOOBAR
