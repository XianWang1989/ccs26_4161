
import os
import sys

# Set the path to your project
sys.path.append('/path/to/your/django/project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
