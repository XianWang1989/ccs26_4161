
import os
import sys

# Set the PATH to your virtual environment
activate_this = '/var/www/wsgi/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Add your application directory to the Python path
sys.path.insert(0, '/path/to/your/application')

# Import your Pyramid application
from myapp import main as app

# Set the application callable for WSGI
application = app()
