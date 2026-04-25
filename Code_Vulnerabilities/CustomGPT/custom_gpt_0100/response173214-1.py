
# Example command to install the requests library
import os

# Ensure you have the right permissions (run as admin if necessary)
os.system('pip install requests')

# Verify installation
import requests

print(requests.__version__)
