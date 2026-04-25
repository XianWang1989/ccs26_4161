
import subprocess as sp

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

# Initialize an empty list to store process outputs
proc_out_list = []

for e in piv_id_list:
    # Run the ls command with wildcard expansion via shell
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and errors
    out, err = proc_out.communicate()

    # Append the output to the list
    proc_out_list.append(out.decode('utf-8'))

    # Print output or error
    if out:
        print(out.decode('utf-8'))
    if err:
        print(f"Error: {err.decode('utf-8')}")

# Now proc_out_list contains the output of each command
