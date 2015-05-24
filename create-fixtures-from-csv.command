#!/bin/bash

echo
cd $(dirname "$0")
python csv_to_json.py question-draft1.csv answer-draft1.csv >> appcode/fixtures/initial_data.json

read -p "Press Enter to close this window" FOOBAR
