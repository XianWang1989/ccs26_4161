
import os
import stat

# Path to your static files
static_dir = '/path/to/static'

# Change permissions
for root, dirs, files in os.walk(static_dir):
    for name in files:
        file_path = os.path.join(root, name)
        # Set permissions to 644
        os.chmod(file_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IWUSR)

    for name in dirs:
        dir_path = os.path.join(root, name)
        # Set permissions to 755
        os.chmod(dir_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
