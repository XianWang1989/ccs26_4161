
import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/path/to/myproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

application = get_wsgi_application()
