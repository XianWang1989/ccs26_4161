
import os
import sys

# Add your project directory to the sys.path
sys.path.append('/path/to/your/django/project')
sys.path.append('/path/to/your/venv/lib/python3.x/site-packages')

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
