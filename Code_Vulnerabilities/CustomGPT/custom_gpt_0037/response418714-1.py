
import subprocess as sp

input_dir = '/path/to/directory'  # Set your input directory here
piv_id_list = ['1000', '1001']  # Example list of account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

# Loop through the account numbers
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'  # Construct the command
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture output and errors

    print(out.decode())  # Print the output
    if err:
        print(f'Error: {err.decode()}')  # Print any errors

