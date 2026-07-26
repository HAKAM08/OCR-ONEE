#!/bin/sh

set -e

echo "Waiting for PostgreSQL..."

until python -c "
import socket
socket.create_connection(('postgres', 5432), timeout=2)
print('PostgreSQL is ready')
" >/dev/null 2>&1
do
    sleep 2
done

echo "PostgreSQL is ready."

echo "Waiting for Elasticsearch..."

until curl -s http://elasticsearch:9200 >/dev/null
do
    sleep 2
done

echo "Elasticsearch is ready."

echo "Running database migrations..."

alembic upgrade head

echo "Starting FastAPI..."

exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000