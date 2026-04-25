
import os
import sys

# Path to your project
sys.path.append('/path/to/your/project')

# Set the settings module for the Django application
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project_name.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
