#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python csv_to_json.py scripts/question-draft1.csv scripts/answer-draft1.csv >> appcode/fixtures/initial_data.json

read -p "Press Enter to close this window" FOOBAR
