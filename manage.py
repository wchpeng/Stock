#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    env = os.environ.get("PY3_DJANGO2_SETTING_ENV", "develop")
    print("-------------------------------")
    print(env)
    print("-------------------------------")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Stock.%s' % env)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
