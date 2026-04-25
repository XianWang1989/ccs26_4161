
import subprocess as sp

input_dir = '/path/to/directory'  # Set your input directory path
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'cd {input_dir} && ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
