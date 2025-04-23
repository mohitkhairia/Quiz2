#!/usr/bin/env sh
# entrypoint.sh
set -e

# wait for db to be ready (optional)
# or add a small sleep if needed

echo "Running migrations…"
python manage.py migrate --noinput

echo "Collecting static…"
python manage.py collectstatic --noinput

exec "$@"