
import subprocess as sp
import os

# Define your input directory and piv_id_list
input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # add your actual account numbers here

# Change to the input directory
os.chdir(input_dir)

# Create an empty list to store the output of subprocesses
proc_out_list = []

# Loop through the piv_id_list
for e in piv_id_list:
    # Use shell=True to enable wildcard expansion
    cmd = 'ls -lh *CSV*APP*{0}.zip'.format(e)

    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and error

    # Append the output to the list
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))

    # Print the output and error (if any)
    print(f'Output for *CSV*APP*{e}.zip:\n{out.decode("utf-8")}\nError (if any):\n{err.decode("utf-8")}')

# Note: Make sure to handle the cases when no files match and errors might arise.
