
import os
import sys
import shutil

def setup_chroot(chroot_dir, files):
    # Create the chroot directory
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy files into the chroot directory
    for file in files:
        shutil.copy(file, chroot_dir)

def main():
    chroot_dir = "/path/to/chroot"  # Specify your chroot directory
    files_to_copy = ["/bin/bash", "/lib/x86_64-linux-gnu/libc.so.6"]  # Example files; adjust as needed

    setup_chroot(chroot_dir)

    # Change root
    os.chroot(chroot_dir)

    # Change to root of new filesystem
    os.chdir("/")

    # Execute the shell, replacing the current process
    os.execvp("bash", ["bash"])

if __name__ == "__main__":
    main()
