
import subprocess as sp
import glob
import os

input_dir = 'path/to/your/directory'  # Set your input directory path
piv_id_list = ['1000', '1001']  # List of account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to find the matching files
    pattern = f"*CSV*APP*{e}.zip"
    matching_files = glob.glob(pattern)

    if matching_files:
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            proc_out_list.append(proc_out)
            output, error = proc_out.communicate()  # Capture output and error
            print(output.decode().strip())  # Print output
            if error:
                print(error.decode().strip())  # Print error if exists
    else:
        print(f"No files found for pattern: {pattern}")
