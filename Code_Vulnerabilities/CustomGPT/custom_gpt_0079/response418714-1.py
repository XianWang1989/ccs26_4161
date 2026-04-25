
import subprocess as sp
import os

# Change to the desired directory
input_dir = '/path/to/your/input_dir'
os.chdir(input_dir)

# List to hold output for each account
proc_out_list = []

# Loop through each account number
piv_id_list = ['1000', '1001', '1002']  # Replace with actual IDs
for e in piv_id_list:
    file_pattern = f"*CSV*APP*{e}.zip"  # Construct the file pattern
    # Run the ls command with shell=True to enable wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', file_pattern], shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(f"Error: {stderr.decode()}")
