
import subprocess as sp

# Define the directory and the list of account numbers
input_dir = '/path/to/directory'
piv_id_list = ['1000', '2000', '3000']  # Example ID list
proc_out_list = []

for e in piv_id_list:
    # Build the command
    command = ['ls', '-lh', f'*CSV*APP*{e}.zip']

    # Execute the command in the specified directory
    proc_out = sp.Popen(command, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and errors
    stdout, stderr = proc_out.communicate()

    # Decode and print results
    if stdout:
        print("Output:\n", stdout.decode())
    if stderr:
        print("Error:\n", stderr.decode())
