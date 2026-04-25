
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Set your directory path here
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to handle wildcard expansion
    file_pattern = f'*CSV*APP*{e}.zip'
    matched_files = sp.check_output(['ls', '-lh', file_pattern], shell=True)

    # Decode the output and display it
    print(matched_files.decode())
    proc_out_list.append(matched_files)

