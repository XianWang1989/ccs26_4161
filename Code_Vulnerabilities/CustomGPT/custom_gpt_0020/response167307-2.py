
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Now PYTHONPATH will include the paths defined in the .env file
for path in os.environ.get('PYTHONPATH', '').split(os.pathsep):
    if path and path not in sys.path:
        sys.path.append(path)

# You can now import your modules
import your_module
