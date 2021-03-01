#!/bin/sh
exec gunicorn -b :5000 --access-logfile - --error-logfile - run:app && rq worker microblog-tasks -u redis://redis:6379/0