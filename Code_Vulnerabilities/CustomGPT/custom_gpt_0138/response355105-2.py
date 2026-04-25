
import os
import subprocess

services = ['apache2', 'celery']

for service in services:
    status = subprocess.run(['systemctl', 'is-active', service], stdout=subprocess.PIPE)
    print(f"{service} is {'running' if status.stdout.decode().strip() == 'active' else 'not running'}")
