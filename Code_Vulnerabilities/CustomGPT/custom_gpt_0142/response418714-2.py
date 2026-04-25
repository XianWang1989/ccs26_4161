
import subprocess as sp
import glob
import os

# Sample input_dir and piv_id_list for demonstration purposes
input_dir = '/path/to/directory'  # Set your target directory
piv_id_list = ['1000', '1001']     # Sample account numbers
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

# Run the ls command for each account number
for e in piv_id_list:
    pattern = "*CSV*APP*{0}.zip".format(e)
    for filename in glob.glob(pattern):  # Get a list of files matching the pattern
        # Call ls on the individual file
        proc_out = sp.Popen(['ls', '-lh', filename], stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = proc_out.communicate()  # Get the output and errors
        proc_out_list.append(out)
        if err:  # Check for and print errors
            print(f"Error: {err.decode()}")
        else:
            print(out.decode())  # Print the output
