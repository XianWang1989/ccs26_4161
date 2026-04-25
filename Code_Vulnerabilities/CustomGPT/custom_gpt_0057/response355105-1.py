
import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def restart_apache():
    logging.info("Restarting Apache2...")
    process = subprocess.run(["sudo", "service", "apache2", "restart"], capture_output=True, text=True)
    if process.returncode == 0:
        logging.info("Apache2 restarted successfully.")
    else:
        logging.error(f"Error restarting Apache2: {process.stderr}")

def collect_static_files():
    logging.info("Collecting static files...")
    process = subprocess.run(["yes", "yes", "|", "sudo", "-u", "www-data", "python3", "manage.py", "collectstatic"], capture_output=True, text=True)
    if process.returncode == 0:
        logging.info("Static files collected successfully.")
    else:
        logging.error(f"Error collecting static files: {process.stderr}")

if __name__ == "__main__":
    collect_static_files()
    restart_apache()
