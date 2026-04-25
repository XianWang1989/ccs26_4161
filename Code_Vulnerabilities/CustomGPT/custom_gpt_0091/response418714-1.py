
import subprocess as sp
import os

# Change to the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)

proc_out_list = []
piv_id_list = ['1000', '1001']  # Example list of account numbers

for e in piv_id_list:
    # Construct the command
    command = f'ls -lh *CSV*APP*{e}.zip'

    # Run the command
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    # Handle the output
    if stdout:
        print(stdout.decode())
    if stderr:
        print(f'Error: {stderr.decode()}')
