
import subprocess as sp
import os

# Set your input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)  # Change the current working directory

proc_out_list = []  # Initialize an empty list to store process outputs
piv_id_list = ['1000', '1001']  # Sample account numbers

# Loop through the list of account numbers
for i, e in enumerate(piv_id_list):
    # Prepare the file pattern
    file_pattern = f"*CSV*APP*{e}.zip"
    # Run the ls command
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Get the output and error messages

    if proc_out.returncode == 0:
        print(stdout.decode())  # Print the found files
    else:
        print(f"Error: {stderr.decode()}")  # Print the error message

