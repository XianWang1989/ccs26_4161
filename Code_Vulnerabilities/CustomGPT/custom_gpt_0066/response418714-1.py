
import subprocess as sp

input_dir = '/path/to/directory'  # Change this to your input directory
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

# Change directory using an absolute path
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    output, error = proc_out.communicate()

    if proc_out.returncode == 0:
        print(output.decode())
    else:
        print(f"Error: {error.decode()}")
