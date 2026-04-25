
import os
import shutil
import subprocess
import sys

def setup_chroot(chroot_dir, source_files):
    # Step 1: Create the chroot directory
    os.makedirs(chroot_dir, exist_ok=True)

    # Step 2: Copy necessary files
    for file in source_files:
        shutil.copy(file, chroot_dir)

    # Step 3: Change root and enter shell
    os.chroot(chroot_dir)
    os.chdir('/')

    # Replace the Python process with the chroot shell
    # Change '/bin/bash' to your desired shell if needed
    os.execv('/bin/bash', ['/bin/bash'])

if __name__ == "__main__":
    chroot_directory = "/path/to/chroot"
    files_to_copy = ["file1", "file2"]  # Replace with actual files

    setup_chroot(chroot_directory, files_to_copy)
