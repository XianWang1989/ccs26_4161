
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Replace with your directory path
piv_id_list = [1000, 1001, 1002]  # Sample list of account numbers
proc_out_list = []

# Change the directory to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the search pattern
    pattern = f"*CSV*APP*{e}.zip"

    # Run the ls command
    proc_out = sp.Popen(['ls', '-lh', pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()

    # Check if there was an error
    if error:
        print(f"Error: {error.decode().strip()}")
    else:
        print(output.decode())

    proc_out_list.append(proc_out)
