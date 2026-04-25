
import os
import shutil
import subprocess
import sys

def setup_chroot(chroot_dir, files_to_copy):
    # Create the chroot directory if it doesn't exist
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy specified files to the chroot directory
    for file in files_to_copy:
        shutil.copy(file, chroot_dir)

    # Execute the chroot command, replacing the current process
    os.execvp("chroot", ["chroot", chroot_dir, "/bin/bash"])

if __name__ == "__main__":
    chroot_directory = "/path/to/chroot"
    files = ["/path/to/file1", "/path/to/file2"]  # List of files to copy

    setup_chroot(chroot_directory, files)

    # After execvp, the following lines won't be executed.
    sys.exit(0)
