
import subprocess as sp

input_dir = '/path/to/directory'  # Update this to your target directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change directory
sp.call(['cd', input_dir], shell=True)

# List files for each account number
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()
    proc_out_list.append(stdout.decode().strip())
    if proc_out.returncode != 0:
        print(f"Error: {stderr.decode().strip()}")
    else:
        print(stdout.decode().strip())

# Print the output list
for output in proc_out_list:
    print(output)
