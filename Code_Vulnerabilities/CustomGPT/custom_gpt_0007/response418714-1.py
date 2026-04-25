
import subprocess as sp
import glob
import os

# Assuming input_dir is the directory you want to search in
input_dir = '/path/to/directory'
os.chdir(input_dir)  # Change the current working directory

piv_id_list = [1000, 1001, 1002]  # Example list of account numbers
proc_out_list = []

for e in piv_id_list:
    # Create the wildcard pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)
    # Expand the wildcard pattern
    matching_files = glob.glob(pattern)

    if matching_files:  # Check if any files matched the pattern
        for file in matching_files:
            # Call `ls -lh` on each matched file
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE)
            stdout, stderr = proc_out.communicate()  # Wait for the process to complete
            print(stdout.decode())  # Print the output from ls
            proc_out_list.append(proc_out)
    else:
        print(f'No files found for pattern: {pattern}')
