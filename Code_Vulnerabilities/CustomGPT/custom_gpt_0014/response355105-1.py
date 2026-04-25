
import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
sys.path.append('/path/to/your/project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

application = get_wsgi_application()
