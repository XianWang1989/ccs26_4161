
from dotenv import load_dotenv
import os

load_dotenv()
pythonpath = os.getenv('PYTHONPATH')

if pythonpath:
    sys.path.extend(pythonpath.split(':'))
