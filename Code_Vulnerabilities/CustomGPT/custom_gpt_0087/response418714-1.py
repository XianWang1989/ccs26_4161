
import os
import subprocess as sp

# Change this to your desired directory
input_dir = '/path/to/directory'
os.chdir(input_dir)

piv_id_list = ['1000', '1001']  # Example IDs
proc_out_list = []

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # capture output and error

    if proc_out.returncode == 0:
        print(out.decode())  # Print the output
    else:
        print(f'Error: {err.decode()}')  # Print the error message
