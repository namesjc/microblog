#!/bin/sh
exec gunicorn -c gunicorn_config.py -b :5000 --access-logfile - --error-logfile - run:app & python worker.py
