
import subprocess as sp

input_dir = "/path/to/directory"
piv_id_list = [1000, 1001, 1002]  # Sample list of IDs

# Change to the specified directory
sp.call(['cd', input_dir], shell=True)

# List to store process outputs
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    # Print output and error
    print(out.decode())  # To see any files listed
    if err:
        print(err.decode())  # To see any errors

