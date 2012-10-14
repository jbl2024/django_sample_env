#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname, join

PROJECT_ROOT = abspath(dirname(__file__))

# Uncomment this if you use Virtualenv
#
activate_this = PROJECT_ROOT + "/../vtenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, join(PROJECT_ROOT, "apps"))

# Normal django...

if 'DJANGO_MODE' not in os.environ:
    os.environ['DJANGO_MODE'] = 'local'
    warning = "------------------------------------------------------------------------------\n"
    warning += " Manage in LOCAL mode : set DJANGO_MODE env variable for prod and dev servers.\n"
    warning += " See README for more informations\n"
    warning += "------------------------------------------------------------------------------\n"
    sys.stderr.write(warning)
    #from time import sleep
    #sleep(1)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
