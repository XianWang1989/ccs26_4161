
import os
import subprocess

def manage_static_files():
    # Collect static files
    try:
        subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)
        print("Static files collected successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error collecting static files: {e}")

if __name__ == "__main__":
    manage_static_files()
