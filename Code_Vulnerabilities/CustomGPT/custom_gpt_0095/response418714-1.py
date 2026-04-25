
import subprocess as sp
import shlex

input_dir = '/path/to/your/directory'  # Set your input directory here
piv_id_list = ['1000', '1001']  # Sample list of account numbers
proc_out_list = []

# Change to the input directory first
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Get output and error (if any)

    if proc_out.returncode == 0:
        proc_out_list.append(out.decode())
        print(out.decode())
    else:
        print(err.decode())
