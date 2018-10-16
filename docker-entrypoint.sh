#!/bin/bash

sleep 5

# Collect static files
echo "Collect static files"
python code/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python code/manage.py makemigrations
python code/manage.py migrate
python code/manage.py migrate --run-syncdb

# Start server
echo "Starting server"
python code/manage.py runserver 0.0.0.0:8080