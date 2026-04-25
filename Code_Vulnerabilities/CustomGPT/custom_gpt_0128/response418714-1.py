
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = [1000, 1001, 1002]  # Example list of account numbers
proc_out_list = []

for e in piv_id_list:
    # Build the command for each account number
    command = ['ls', '-lh', f'*CSV*APP*{e}.zip']

    # Execute the command in the correct directory
    proc_out = sp.Popen(command, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Wait for the command to finish

    # Print the output or error
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

    proc_out_list.append(proc_out)

print(proc_out_list)
