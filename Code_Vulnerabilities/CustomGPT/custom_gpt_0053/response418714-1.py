
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Update with your directory path
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    # Using shell=True to allow wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    try:
        proc_out = sp.check_output(command, shell=True, text=True)
        proc_out_list.append(proc_out)
        print(proc_out)
    except sp.CalledProcessError as e:
        print(f"Error: {e.output}")  # Printing error if the file is not found
