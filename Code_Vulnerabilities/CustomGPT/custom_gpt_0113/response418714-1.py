
import subprocess as sp

# Directory where the files are located
input_dir = '/path/to/directory'
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Construct the ls command using shell globbing
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and error
    output, error = proc_out.communicate()
    proc_out_list.append((output.decode(), error.decode()))

    # Print the outputs or errors
    if output:
        print(output.decode())
    if error:
        print(error.decode())
