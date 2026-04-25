
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Specify your input directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use shell=True for wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and errors
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(f"Error: {stderr.decode()}")
