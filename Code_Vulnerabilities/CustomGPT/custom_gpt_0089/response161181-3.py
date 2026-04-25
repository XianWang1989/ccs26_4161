
import sys
import os

# Add the app's directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'path/to/your/apps'))

# Now you can import your models
from tribes.models import YourModel
