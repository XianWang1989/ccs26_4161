
import subprocess as sp
import os

input_dir = 'your_directory'  # Replace with your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use wildcard expansion with the shell
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture the output and error

    if proc_out.returncode == 0:
        print(stdout.decode())  # Print the output
    else:
        print(f'Error: {stderr.decode()}')  # Print the error message
