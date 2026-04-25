
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Change to your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Loop through each account number
for e in piv_id_list:
    # Construct the file search pattern
    file_pattern = f'*CSV*APP*{e}.zip'

    # Use Popen with the cwd argument to set the working directory
    proc_out = sp.Popen(['ls', '-lh', file_pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()  # Get stdout and stderr

    # Store the output or handle it as needed
    proc_out_list.append((output.decode(), error.decode()))
    print(output.decode())  # Print standard output
    print(error.decode())    # Print any errors
