
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Change this to your desired directory
piv_id_list = [1000, 1001]  # List of account numbers
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Get output and errors
    proc_out_list.append(stdout.decode().strip())  # Decode and store output
    if stderr:
        print(f"Error: {stderr.decode().strip()}")  # Print any errors

# Print the output from the ls command
for output in proc_out_list:
    print(output)
