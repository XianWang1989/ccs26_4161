
import subprocess as sp
import os

# Set the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)  # Change to the target directory

proc_out_list = []  # Initialize the list to store process outputs
piv_id_list = ['1000', '1001']  # Example account numbers

for e in piv_id_list:
    # Use glob to expand the wildcard
    file_pattern = '*CSV*APP*{0}.zip'.format(e)
    matching_files = sp.run(['ls', '-lh', file_pattern], capture_output=True, text=True)

    if matching_files.returncode == 0:
        print(matching_files.stdout)  # Print the output if successful
    else:
        print(matching_files.stderr)  # Print the error if not successful
