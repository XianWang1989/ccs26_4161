
import os
import sys

# Path to your project
project_path = '/path/to/your/django/project'
if project_path not in sys.path:
    sys.path.append(project_path)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
