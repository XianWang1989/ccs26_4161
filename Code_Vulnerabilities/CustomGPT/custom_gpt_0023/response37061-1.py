
import os
import subprocess
import sys
import shutil

def setup_chroot(chroot_dir, files_to_copy):
    # Create chroot directory if it doesn't exist
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy required files to the chroot directory
    for file in files_to_copy:
        shutil.copy(file, chroot_dir)

    # Now invoke chroot
    try:
        # Use os.execvp to replace the Python process with the chroot shell
        os.chroot(chroot_dir)
        os.chdir('/')  # Change to the new root

        # Execute a shell within the chroot
        os.execvp('bash', ['bash'])
    except Exception as e:
        print(f"Error entering chroot: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    chroot_directory = '/path/to/chroot'  # Define your chroot directory
    files_needed = ['/path/to/file1', '/path/to/file2']  # Files to copy into chroot

    setup_chroot(chroot_directory, files_needed)
