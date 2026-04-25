
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the command
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Get the output and errors
    stdout, stderr = proc_out.communicate()

    # Print the output
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
