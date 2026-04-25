
import os
import subprocess

# Define the path to your static files directory
staticfiles_dir = '/path/to/static/files/'

# Ensure the web server has the right permissions
subprocess.run(['sudo', 'chown', '-R', 'www-data:www-data', staticfiles_dir])
subprocess.run(['sudo', 'chmod', '-R', '755', staticfiles_dir])

# Collect static files
os.system('yes | python manage.py collectstatic --noinput')
