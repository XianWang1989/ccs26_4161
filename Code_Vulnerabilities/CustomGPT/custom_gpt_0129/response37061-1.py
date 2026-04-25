
import os
import sys
import shutil

def setup_chroot(new_root, files_to_copy):
    # Create the new root directory
    os.makedirs(new_root, exist_ok=True)

    # Copy necessary files to the new root (e.g., /bin, /lib, /lib64)
    for src in files_to_copy:
        dest = os.path.join(new_root, os.path.basename(src))
        shutil.copytree(src, dest)

    # Execute the chroot
    os.chroot(new_root)
    os.chdir('/')  # change directory to the new root after chroot

    # Replace this process with a new shell
    os.execvp('bash', ['bash'])

if __name__ == "__main__":
    # Define the new root directory and files to copy
    new_root = '/path/to/new_root'
    files_to_copy = ['/bin/bash', '/lib/x86_64-linux-gnu/libc.so.6', '/lib64/ld-linux-x86-64.so.2']  # Example files

    setup_chroot(new_root, files_to_copy)
