
import os
import shutil
import sys
import subprocess

def prepare_chroot_environment(chroot_dir):
    # Perform necessary setup here, such as copying files
    # For example, copying a needed file to the chroot directory
    os.makedirs(chroot_dir, exist_ok=True)
    shutil.copy('/path/to/file', chroot_dir)  # Change the path as needed

    # You can add other setup operations here

def main(chroot_dir):
    # Prepare the chroot environment
    prepare_chroot_environment(chroot_dir)

    # Change root into the new directory
    os.chroot(chroot_dir)

    # Change the current directory to /
    os.chdir('/')

    # Replace the current Python process with a new shell
    # You can change '/bin/bash' to any shell you prefer
    os.execvp('bash', ['bash'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 chroot_wrapper.py <chroot_directory>")
        sys.exit(1)

    chroot_directory = sys.argv[1]
    main(chroot_directory)
