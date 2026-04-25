
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory path
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

# Iterate over account numbers and construct the command
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())
