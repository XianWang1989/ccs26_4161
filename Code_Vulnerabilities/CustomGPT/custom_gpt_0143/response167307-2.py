
import os

# Set the PYTHONPATH environment variable
os.environ['PYTHONPATH'] = '/path/to/your/directory:/path/to/your/other/directory'

# Now when you import, it includes the specified directories
import your_module
