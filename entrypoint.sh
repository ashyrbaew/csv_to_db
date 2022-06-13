#!/bin/sh

    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done
    echo "PostgreSQL started"

    echo "Migrate the Database at startup of project"
    python manage.py migrate --settings ${DJANGO_SETTINGS_MODULE} --noinput

    echo "Update translation fields"
    python manage.py update_translation_fields --settings ${DJANGO_SETTINGS_MODULE}

    echo "Importing Test data from TEST CSV File__________"
    python manage.py import_csv ./test_data.csv

    echo "Create admin user"
    python manage.py createsuperuser --email=admin@admin.com --noinput

    echo "RUNNING DEV SERVER DJANGO__________"
    python manage.py runserver 0.0.0.0:8000

    echo "Running gunicorn======================"
    gunicorn csv_to_db.wsgi:application --bind 0.0.0.0:8000 --config='/app/csv_to_db/gunicorn.py' --workers=3
