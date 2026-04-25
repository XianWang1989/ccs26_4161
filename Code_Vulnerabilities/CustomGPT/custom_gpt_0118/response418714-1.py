
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Set this to your directory
piv_id_list = ['1000', '1001']  # Replace with your actual account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)

    # Use the 'ls' command with globbing in the shell
    proc_out = sp.Popen(['ls', '-lh', pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode().strip())
    else:
        print(stderr.decode().strip())
