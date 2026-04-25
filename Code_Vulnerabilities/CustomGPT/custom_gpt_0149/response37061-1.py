
import os
import shutil
import subprocess
import sys

def setup_chroot(chroot_dir, files):
    # Create the chroot directory if it doesn't exist
    os.makedirs(chroot_dir, exist_ok=True)

    # Copy required files into the chroot environment
    for src in files:
        dst = os.path.join(chroot_dir, os.path.basename(src))
        shutil.copy(src, dst)

    # Change root and execute a shell
    try:
        # Change root to the new directory
        os.chroot(chroot_dir)

        # Change the working directory to the new root
        os.chdir("/")

        # Execute a shell (e.g., bash)
        os.execv("/bin/bash", ["bash"])
    except Exception as e:
        print(f"Failed to chroot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    chroot_directory = "/path/to/chroot"
    files_to_copy = ["/some/file1", "/some/file2"]

    setup_chroot(chroot_directory, files_to_copy)
