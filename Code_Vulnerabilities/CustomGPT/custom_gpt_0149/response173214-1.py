
# Example of installing a package and importing it in Python
import subprocess

# Installing a package via pip
subprocess.check_call(["python", '-m', 'pip', 'install', 'requests'])

# Importing the installed package
import requests

# Using the requests module to make a GET request
response = requests.get('https://api.github.com')
print(response.json())
