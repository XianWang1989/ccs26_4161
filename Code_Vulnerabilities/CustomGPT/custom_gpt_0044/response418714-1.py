
import subprocess as sp
import os
import glob

# Change to the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)

# Assuming piv_id_list contains your account numbers
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # Construct the search pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)
    # Use glob to find matching files
    matching_files = glob.glob(pattern)

    # Check if files were found
    if matching_files:
        for file in matching_files:
            # Execute the command for each found file
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = proc_out.communicate()  # Capture output and error
            print(out.decode())  # Print the output
            if err:
                print(err.decode())  # Print any errors, if present
    else:
        print(f"No files found matching pattern: {pattern}")
