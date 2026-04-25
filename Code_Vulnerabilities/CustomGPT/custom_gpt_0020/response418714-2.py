
import subprocess as sp
import glob
import os

input_dir = "/path/to/directory"
piv_id_list = [1000, 1001, 1002]  # Sample list of IDs

# Change to the specified directory
os.chdir(input_dir)

# List to store the output
proc_out_list = []

for e in piv_id_list:
    # Use glob to find the pattern
    pattern = f'*CSV*APP*{e}.zip'
    matching_files = glob.glob(pattern)

    if matching_files:
        for f in matching_files:
            # Call ls command for each file if needed or process the file directly
            proc_out = sp.Popen(['ls', '-lh', f], stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = proc_out.communicate()
            print(out.decode())  # Show the file details
            if err:
                print(err.decode())
    else:
        print(f"No files found for pattern: {pattern}")
