
import os
import shutil
import sys

def setup_chroot(new_root, setup_files):
    # Copy files to new root
    for file in setup_files:
        shutil.copy(file, new_root)

    # Change root
    os.chroot(new_root)
    os.chdir("/")  # Change current directory to the new root

    # Execute shell (replace the Python process)
    os.execlp("bash", "bash")

if __name__ == "__main__":
    new_root = "/path/to/new/root"
    setup_files = ["/path/to/setup/file1", "/path/to/setup/file2"]

    # Initial setup
    setup_chroot(new_root, setup_files)
