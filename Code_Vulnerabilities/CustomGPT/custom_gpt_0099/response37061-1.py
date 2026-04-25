
import os
import sys
import shutil

def setup_chroot(chroot_dir, files_to_copy):
    # Creating a new chroot directory
    os.makedirs(chroot_dir, exist_ok=True)

    # Copying necessary files to the chroot directory
    for file in files_to_copy:
        shutil.copy(file, os.path.join(chroot_dir, os.path.basename(file)))

    # Change root to the new directory
    os.chroot(chroot_dir)

    # Change the working directory to the new root
    os.chdir('/')

    # Execute a shell (bash) within the chroot
    os.execvp('bash', ['bash'])

if __name__ == "__main__":
    chroot_directory = '/path/to/new/chroot'
    files_needed = ['/path/to/some/file', '/path/to/another/file']

    setup_chroot(chroot_directory, files_needed)
