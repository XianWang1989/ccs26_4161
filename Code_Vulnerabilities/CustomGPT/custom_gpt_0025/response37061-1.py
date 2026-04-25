
#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess

def setup_chroot_env(new_root):
    """Prepare the chroot environment."""
    # Create necessary directories in the new root
    os.makedirs(os.path.join(new_root, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(new_root, 'lib'), exist_ok=True)
    os.makedirs(os.path.join(new_root, 'lib64'), exist_ok=True)

    # Copy necessary binaries (e.g., /bin/bash) and their dependencies
    shutil.copy('/bin/bash', os.path.join(new_root, 'bin/'))

    # Optionally copy libraries required by the binary
    # This may require additional work to find and copy dependencies
    # For simplicity, we're assuming bash only needs the following
    shutil.copy('/lib/x86_64-linux-gnu/libtinfo.so.6', os.path.join(new_root, 'lib64/'))
    shutil.copy('/lib/x86_64-linux-gnu/libdl.so.2', os.path.join(new_root, 'lib64/'))
    shutil.copy('/lib/x86_64-linux-gnu/libc.so.6', os.path.join(new_root, 'lib64/'))

def main(new_root):
    """Main function to set up chroot and invoke shell."""
    setup_chroot_env(new_root)

    # Change the root directory
    os.chroot(new_root)
    os.chdir('/')  # Change working directory to the new root

    # Execute the shell
    os.execve('/bin/bash', ['/bin/bash'], os.environ)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python chroot_wrapper.py <new_root>")
        sys.exit(1)

    main(sys.argv[1])
