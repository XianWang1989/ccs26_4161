
import os
import stat

# Path to your static files directory
static_dir = '/path/to/your/static/files/'

# Check and adjust permissions
def ensure_permissions(directory):
    # Change ownership to www-data user
    os.system(f"sudo chown -R www-data:www-data {directory}")

    # Change permissions
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

ensure_permissions(static_dir)
