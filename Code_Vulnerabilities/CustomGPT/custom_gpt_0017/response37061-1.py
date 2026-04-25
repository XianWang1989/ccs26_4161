
import os
import subprocess
import shutil
import sys

def setup_chroot(target_dir):
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Copy necessary files or setup here
    # Example: Copy a simple file (you can customize this as needed)
    shutil.copyfile('/etc/hosts', os.path.join(target_dir, 'etc', 'hosts'))

    # Change root and execute bash shell
    os.chroot(target_dir)
    os.chdir('/')  # Change to the new root directory
    subprocess.call(['/bin/bash'])  # Start a new shell

if __name__ == "__main__":
    target_directory = "/path/to/chroot"  # Specify your chroot directory

    setup_chroot(target_directory)

    # Terminate the Python script
    sys.exit()
