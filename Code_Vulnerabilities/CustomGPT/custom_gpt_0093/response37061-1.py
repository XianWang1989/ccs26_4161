
import os
import subprocess
import sys

def setup_chroot_environment(chroot_dir, files_to_copy):
    # Copy files to the chroot directory
    for file in files_to_copy:
        subprocess.run(['cp', file, chroot_dir])

    # Change the root directory
    os.chroot(chroot_dir)
    os.chdir('/')  # Change to the new root

    # Execute a new shell
    os.execve('/bin/bash', ['bash'], os.environ)

if __name__ == "__main__":
    chroot_directory = '/path/to/chroot'
    files_to_copy = ['/path/to/file1', '/path/to/file2']

    setup_chroot_environment(chroot_directory, files_to_copy)
