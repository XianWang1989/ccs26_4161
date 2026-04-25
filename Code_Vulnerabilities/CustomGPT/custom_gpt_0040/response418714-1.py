
import subprocess as sp

input_dir = '/path/to/your/directory'  # Change to your actual directory
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

# Change the directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to expand the wildcard pattern
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture output and errors
    proc_out_list.append(out.decode().strip())  # Store output
    if err:
        print(err.decode().strip())  # Print any error messages
    else:
        print(out.decode().strip())  # Print command output
