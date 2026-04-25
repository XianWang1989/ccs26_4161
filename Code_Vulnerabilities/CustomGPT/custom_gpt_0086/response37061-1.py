
import os
import subprocess
import sys

def setup_chroot(chroot_dir):
    # Step 1: Copy necessary files to chroot directory
    # (Customize this part as needed)
    os.makedirs(os.path.join(chroot_dir, "bin"), exist_ok=True)
    subprocess.run(["cp", "/bin/bash", os.path.join(chroot_dir, "bin")])

    # Step 2: Execute chroot
    os.chroot(chroot_dir)
    os.chdir("/")  # Change the root directory to the new root

    # Step 3: Execute a shell in the new chroot environment
    os.execv("/bin/bash", ["/bin/bash"])  # Replace the current process

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chroot_wrapper.py <chroot_directory>")
        sys.exit(1)

    chroot_directory = sys.argv[1]
    setup_chroot(chroot_directory)
