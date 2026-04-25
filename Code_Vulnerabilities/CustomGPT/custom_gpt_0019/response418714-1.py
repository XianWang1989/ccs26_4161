
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change directory using subprocess
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    out, err = proc_out.communicate()
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))
    print(out.decode('utf-8') if out else err.decode('utf-8'))
