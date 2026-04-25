
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your directory
piv_id_list = ['1000', '2000']  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    command = 'ls -lh {}/CSV*APP*{}.zip'.format(input_dir, e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture the output and errors
    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())
