
import os
import subprocess
import sys

def chroot_wrapper(chroot_path, setup_commands):
    # Execute setup commands
    for command in setup_commands:
        subprocess.run(command, shell=True)

    # Change to the new root directory
    os.chroot(chroot_path)

    # Change the current working directory to the new root
    os.chdir('/')

    # Call the shell
    subprocess.run(['/bin/bash'])

if __name__ == "__main__":
    setup_cmds = [
        "cp /src/file /target/",  # Example file copying command
        "mkdir /target/newdir",    # Example directory creation command
    ]

    chroot_path = "/path/to/chroot"

    # Call the wrapper function
    chroot_wrapper(chroot_path, setup_cmds)
