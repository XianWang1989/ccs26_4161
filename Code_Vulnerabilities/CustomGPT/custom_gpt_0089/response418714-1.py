
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your input directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Build the command as a string
    command = f'ls -lh *CSV*APP*{e}.zip'
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    # We'll store the output and errors if necessary
    if proc_out.returncode == 0:
        proc_out_list.append(out.decode())
    else:
        print(f"Error: {err.decode()}")

# Print the results
for result in proc_out_list:
    print(result)
