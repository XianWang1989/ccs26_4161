
import subprocess as sp
import os

# Set the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)  # Change to the input directory

piv_id_list = ['1000', '2000']  # Example list of account numbers
proc_out_list = []

for e in piv_id_list:
    # Construct the command
    command = f'ls -lh *CSV*APP*{e}.zip'

    # Use shell=True to enable wildcard expansion
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Get the output and error messages

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
