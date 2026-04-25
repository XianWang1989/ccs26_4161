
import subprocess as sp
import os

# Set your input directory
input_dir = 'path/to/your/directory'  # Replace with your actual directory
os.chdir(input_dir)  # Change the working directory

proc_out_list = []
piv_id_list = [1000, 1001, 1002]  # Example account numbers

for e in piv_id_list:
    # Create the command string
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)

    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and error

    if out:
        print(out.decode())  # Print the output
    if err:
        print(err.decode())  # Print the error if any
