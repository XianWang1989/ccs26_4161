
# test_wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
application = get_wsgi_application()

if __name__ == '__main__':
    from wsgi import run_simple
    run_simple('localhost', 8000, application)
