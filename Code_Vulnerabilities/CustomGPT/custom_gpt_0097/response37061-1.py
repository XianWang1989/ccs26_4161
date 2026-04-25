
import os
import sys

def setup_chroot(chroot_dir):
    # Perform setup tasks (copy files, etc.)
    # Example: os.system(f"cp /path/to/file {chroot_dir}/path/in/chroot")

    # Change root to the new directory
    os.chroot(chroot_dir)

    # Change to the new root directory
    os.chdir("/")

    # Replace the current process with a new shell (e.g., /bin/bash)
    os.execlp("bash", "bash")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <chroot_directory>")
        sys.exit(1)

    chroot_directory = sys.argv[1]

    setup_chroot(chroot_directory)
