
import os
import subprocess as sp

input_dir = '/path/to/directory'  # Set your directory path
piv_id_list = ['1000']  # Example list of account numbers
proc_out_list = []

# Change to the directory
os.chdir(input_dir)

for e in piv_id_list:
    # List files that match the pattern
    files = [f for f in os.listdir('.') if f.endswith(f'APP{e}.zip') and 'CSV' in f]
    for file in files:
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        proc_out_list.append(proc_out)
        output, errors = proc_out.communicate()
        print(f"Output:\n{output.decode()}")
        if errors:
            print(f"Errors:\n{errors.decode()}")
