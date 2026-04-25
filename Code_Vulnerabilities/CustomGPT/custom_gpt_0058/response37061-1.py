
import os
import shutil
import sys

def setup_chroot(new_root, bind_dirs):
    # Create the new root directory
    os.makedirs(new_root, exist_ok=True)

    # Copy necessary files to the new root
    for src in bind_dirs:
        dst = os.path.join(new_root, os.path.basename(src))
        shutil.copytree(src, dst, dirs_exist_ok=True)

    # Change the root and execute a shell
    os.chroot(new_root)

    # Switch to the new root directory
    os.chdir("/")

    # Execute the shell (e.g., /bin/bash)
    os.execv('/bin/bash', ['bash'])

if __name__ == "__main__":
    new_root = "/path/to/new/root"  # Set your new root path
    bind_dirs = ['/bin', '/lib', '/lib64', '/usr']  # Directories to bind

    setup_chroot(new_root, bind_dirs)
