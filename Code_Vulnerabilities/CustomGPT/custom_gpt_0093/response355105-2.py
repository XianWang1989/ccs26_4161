
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/path/to/your/project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

application = get_wsgi_application()
