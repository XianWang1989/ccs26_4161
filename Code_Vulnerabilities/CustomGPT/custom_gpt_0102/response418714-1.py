
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

# Loop through the account numbers and execute the ls command
for e in piv_id_list:
    pattern = f'*CSV*APP*{e}.zip'
    # Use shell=True to allow shell wildcard expansion
    proc_out = sp.Popen(f'ls -lh {pattern}', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(f'Error: {stderr.decode()}')
