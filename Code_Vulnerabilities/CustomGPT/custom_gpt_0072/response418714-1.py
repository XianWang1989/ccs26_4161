
import subprocess as sp

# Change to the directory
sp.call(['cd', input_dir], shell=True)

# List to store output
proc_out_list = []

# Iterate through the account numbers
for e in piv_id_list:
    # Construct the command
    command = f'ls -lh *CSV*APP*{e}.zip'
    # Execute the command in the specified directory
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    out, err = proc_out.communicate()

    if proc_out.returncode == 0:
        proc_out_list.append(out.decode())
        print(out.decode())
    else:
        print(f"Error: {err.decode()}")
