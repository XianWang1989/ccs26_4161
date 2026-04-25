
import os
import sys

sys.path.append('/path/to/your/project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
