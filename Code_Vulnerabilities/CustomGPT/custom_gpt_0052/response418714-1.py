
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # Construct the command with wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'

    # Use shell=True to enable wildcard processing
    proc_out = sp.Popen(command, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()

    # Store the output and error
    if output:
        print(output.decode())
    if error:
        print(error.decode())
