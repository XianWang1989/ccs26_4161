
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # specify your directory
piv_id_list = ['1000', '1001', '1002']  # example list of IDs
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Prepare the command with the wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'
    # Run the command through the shell
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture output and errors
    proc_out_list.append(out)

    # Print output or error
    if out:
        print(out.decode())
    if err:
        print(err.decode())
