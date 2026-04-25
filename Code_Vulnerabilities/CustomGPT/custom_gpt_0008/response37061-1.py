
import os
import shutil
import sys

def setup_chroot(chroot_dir, new_root, files_to_copy):
    # Create the chroot directory
    if not os.path.exists(chroot_dir):
        os.makedirs(chroot_dir)

    # Copy necessary files
    for file in files_to_copy:
        shutil.copy(file, os.path.join(chroot_dir, os.path.basename(file)))

    # Change the root directory
    os.chroot(chroot_dir)

    # Change the working directory to the new root
    os.chdir("/")

    # Execute a new shell (e.g., bash) in the chroot environment
    os.execv("/bin/bash", ["/bin/bash"])

if __name__ == "__main__":
    # Example usage
    chroot_directory = "/path/to/chroot"
    files_to_copy = ["/etc/hostname", "/etc/hosts"]  # Add necessary files here

    setup_chroot(chroot_directory, "/new/root", files_to_copy)
