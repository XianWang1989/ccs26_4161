
import os
import sys

# Add your project directory to the sys.path
sys.path.append('/path/to/myproject')
sys.path.append('/path/to/myproject/myproject')

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
