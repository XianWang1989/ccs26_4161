
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

# Change to input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
