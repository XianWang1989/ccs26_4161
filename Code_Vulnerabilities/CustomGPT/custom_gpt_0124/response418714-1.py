
import subprocess as sp
import glob
import os

input_dir = '/path/to/directory'  # Specify your directory here
piv_id_list = ['1000', '1001']  # Example list of account numbers
proc_out_list = []

# Change directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to find the matching files
    pattern = f'*CSV*APP*{e}.zip'
    files = glob.glob(pattern)

    if files:
        for file in files:
            # Call ls command on the found file
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = proc_out.communicate()
            print(output.decode() if output else error.decode())
    else:
        print(f"No matching files found for pattern: {pattern}")
