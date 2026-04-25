
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
sys.path.append('/path/to/your/project')

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Get the WSGI application
application = get_wsgi_application()
