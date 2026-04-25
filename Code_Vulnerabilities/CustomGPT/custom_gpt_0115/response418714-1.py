
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    pattern = '*CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(['ls', '-lh', pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
