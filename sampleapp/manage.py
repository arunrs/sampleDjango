#!/usr/bin/env python
import os
import sys
from collections import defaultdict
from datetime import datetime

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sampleapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
