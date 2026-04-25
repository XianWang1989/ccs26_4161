
import os
import shutil
import subprocess
import sys

def setup_chroot(chroot_dir, files_to_copy):
    # Create the chroot directory if it doesn't exist
    if not os.path.exists(chroot_dir):
        os.makedirs(chroot_dir)

    # Copy specified files to the chroot directory
    for file in files_to_copy:
        shutil.copy(file, chroot_dir)

    # Change root and exec a new shell
    os.chroot(chroot_dir)
    os.chdir('/')

    # Replace the Python process with a new shell
    subprocess.run(['bash'])

if __name__ == "__main__":
    # Specify the chroot directory and files to copy
    chroot_directory = '/path/to/chroot'
    files_to_copy = ['/etc/passwd', '/etc/group']  # Example files

    setup_chroot(chroot_directory, files_to_copy)
    sys.exit(0)  # Ensure the script exits after setup
