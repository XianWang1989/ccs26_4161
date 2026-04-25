
import os
import shutil
import sys

def setup_chroot(chroot_dir, source_files):
    # Copy files into the chroot directory
    for file in source_files:
        shutil.copy(file, os.path.join(chroot_dir, os.path.basename(file)))

    # Change root to the new directory
    os.chroot(chroot_dir)
    os.chdir("/")  # Change to the new root directory

    # Execute a shell inside the chroot
    os.execlp("bash", "bash")  # Replace the current process with a bash shell

if __name__ == "__main__":
    chroot_directory = "/path/to/new/chroot"  # Specify your chroot directory
    files_to_copy = ["/path/to/file1", "/path/to/file2"]  # List your files here

    setup_chroot(chroot_directory, files_to_copy)
