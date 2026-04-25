
import os
import subprocess
import sys
import shutil

def setup_chroot(chroot_dir, files_to_copy):
    # Create chroot directory
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy necessary files to chroot directory
    for file in files_to_copy:
        shutil.copy(file, chroot_dir)

    # Change root directory
    os.chroot(chroot_dir)

    # Execute a shell inside the new root environment
    os.execvp("bash", ["bash"])

if __name__ == "__main__":
    chroot_directory = "/path/to/chroot"
    files_needed = ["/bin/bash", "/lib64/ld-linux-x86-64.so.2", "/lib64/libc.so.6"]  # Adjust accordingly

    setup_chroot(chroot_directory, files_needed)
