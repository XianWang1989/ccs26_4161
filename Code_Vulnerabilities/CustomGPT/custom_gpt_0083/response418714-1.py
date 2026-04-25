
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Specify your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
