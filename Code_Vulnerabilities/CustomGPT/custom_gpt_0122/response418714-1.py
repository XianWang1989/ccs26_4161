
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your directory path
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change the working directory
sp.Popen(['cd', input_dir], shell=True)

# List files for each account number
for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
