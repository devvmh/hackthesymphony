#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangostuff.settings")

    from django.core.management import execute_from_command_line

    #auto 0.0.0.0:8000
    args = sys.argv[:]
    if len(args) == 2 and sys.argv[1] == 'runserver':
      args = sys.argv + ['0.0.0.0:8000']

    execute_from_command_line(args)
