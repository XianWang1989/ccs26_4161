
import sys
import os

activate_this = '/path/to/your/virtualenv/bin/activate_this.py'
exec(open(activate_this, 'rt').read(), dict(__file__=activate_this))

# Rest of your WSGI application code...
