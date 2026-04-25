
import os
import subprocess as sp

input_dir = '/path/to/your/directory'  # Change to your actual directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    if out:
        print(out.decode())
    if err:
        print(err.decode())
