#!/bin/bash

echo
cd $(basename "$0")
python scripts/csv_to_json.py scripts/questions-draft1.csv scripts/answers-draft1.csv > appcode/fixtures/initial_data.json
sed -i '' -e 's/\]/,/' appcode/fixtures/initial_data.json
cat scripts/concert-fixtures.json >> appcode/fixtures/initial_data.json
echo "]" >> appcode/fixtures/initial_data.json

read -p "Press Enter to close this window" FOOBAR
