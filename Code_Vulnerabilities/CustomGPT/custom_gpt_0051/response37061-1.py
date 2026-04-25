
import os
import subprocess
import sys

def setup_chroot(chroot_dir):
    # Copy files or perform any setup needed here
    # Example: subprocess.run(['cp', 'somefile', chroot_dir])

    # Change root
    os.chroot(chroot_dir)

    # Change the working directory to the new root
    os.chdir('/')

    # Execute a new shell
    os.execlp('bash', 'bash')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 chroot_wrapper.py <chroot_directory>")
        sys.exit(1)

    chroot_directory = sys.argv[1]

    # Ensure the chroot directory exists
    if not os.path.isdir(chroot_directory):
        print(f"Error: {chroot_directory} does not exist.")
        sys.exit(1)

    setup_chroot(chroot_directory)
