
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your directory path
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    cmd = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
