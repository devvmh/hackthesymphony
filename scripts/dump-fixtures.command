#!/bin/bash

echo
cd $(dirname "$0")/..
python manage.py dumpdata --indent 2 appcode.Question appcode.Answer appcode.Concert appcode.ConcertAnswerScore > appcode/fixtures/fixtures.json
