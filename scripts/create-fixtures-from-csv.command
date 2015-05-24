#!/bin/bash

echo
cd $(find ~ -name hackthesymphony)
python scripts/csv_to_json.py scripts/questions-draft1.csv scripts/answers-draft1.csv > appcode/fixtures/initial_data.json

read -p "Press Enter to close this window" FOOBAR
