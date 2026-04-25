
import subprocess as sp
import os

input_dir = '/path/to/directory'  # Set your input directory here
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the command string with wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'
    try:
        # Execute the command using shell=True
        proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = proc_out.communicate()  # Get the output and errors

        # Append output to list
        proc_out_list.append(stdout.decode().strip())

        if stderr:
            print(f"Error: {stderr.decode().strip()}")  # Print any error messages
        else:
            print(stdout.decode().strip())  # Print the successful output

    except Exception as e:
        print(f"An error occurred: {e}")
