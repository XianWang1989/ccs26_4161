
import os
import shutil
import sys

def setup_chroot(target_dir, files_to_copy):
    # Create the new chroot environment
    os.makedirs(target_dir, exist_ok=True)

    # Copy files to the new environment
    for file in files_to_copy:
        shutil.copy(file, target_dir)

    # Change to the new directory for chroot
    os.chroot(target_dir)
    os.chdir('/')

    # Replace the current process with a new shell
    os.execvp('bash', ['bash'])

if __name__ == "__main__":
    # Specify the chroot target directory and files to copy
    target_directory = '/path/to/chroot'
    files = ['file1.txt', 'file2.txt']

    setup_chroot(target_directory, files)
