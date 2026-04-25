
import subprocess as sp
import os

input_dir = '/path/to/directory'  # Set your input directory here
piv_id_list = ['1000', '2000']  # Example account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    try:
        proc_out = sp.check_output(command, shell=True, text=True)
        proc_out_list.append(proc_out)
        print(proc_out)
    except sp.CalledProcessError as e:
        print(f'Error: {e}')

# Now proc_out_list contains the results of the ls command
