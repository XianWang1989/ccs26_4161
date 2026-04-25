
import os
import sys
import shutil

def setup_chroot(chroot_dir):
    # Perform your setup tasks here
    print("Copying files...")
    shutil.copy('/path/to/source/file', chroot_dir + '/path/to/dest/')

    # More setup tasks as needed...

    # Change root and execute shell
    os.chroot(chroot_dir)  # Change the root directory
    os.chdir('/')          # Change to the new root

    # Replace the current process with a new shell
    os.execlp('bash', 'bash')  # or use '/bin/bash' if you need the full path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <chroot_directory>")
        sys.exit(1)

    chroot_directory = sys.argv[1]

    if not os.path.isdir(chroot_directory):
        print(f"{chroot_directory} is not a valid directory.")
        sys.exit(1)

    setup_chroot(chroot_directory)
