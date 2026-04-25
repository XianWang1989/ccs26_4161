
# Commands to restart the Django service and collect static files

# Run ZEO
runzeo -a localhost:8090 -f /path/to/operations_cache.fs

# Switch to the project owner's user
su project_owner

# Start Celery workers with debug logging
python manage.py celery worker -n multiprocessing_worker --loglevel=debug -Q multiprocessing_queue
python manage.py celery worker --concurrency=500 --pool=eventlet --loglevel=debug -Q celery -n eventlet_worker
