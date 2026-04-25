
import subprocess as sp

input_dir = '/path/to/your/input/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    out, err = proc_out.communicate()
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))
    print(out.decode('utf-8'), err.decode('utf-8'))
