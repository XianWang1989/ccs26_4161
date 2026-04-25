
import os
import shutil
import sys

def setup_chroot(chroot_dir, files_to_copy):
    # Create the chroot environment
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy necessary files into the chroot directory
    for file in files_to_copy:
        shutil.copy(file, chroot_dir)

    # Change root and execute shell
    os.chroot(chroot_dir)
    os.execvp("/bin/bash", ["bash"])

if __name__ == "__main__":
    chroot_directory = "/path/to/chroot"
    files_to_copy = ["/etc/passwd", "/etc/group"]  # Add necessary files

    setup_chroot(chroot_directory, files_to_copy)
