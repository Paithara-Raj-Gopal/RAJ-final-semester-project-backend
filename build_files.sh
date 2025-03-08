#!/bin/bash
echo " BUILD START"

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

# Apply database migrations
python manage.py migrate

echo " BUILD END"