
import subprocess as sp
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

# Change directory
os.chdir(input_dir)

for e in piv_id_list:
    # Create the command with the wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'

    # Use subprocess with shell=True to interpret the wildcard
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    # Append the output to the list
    proc_out_list.append(proc_out.stdout)

    # Print the output or error
    if proc_out.returncode == 0:
        print(proc_out.stdout)
    else:
        print(proc_out.stderr)
