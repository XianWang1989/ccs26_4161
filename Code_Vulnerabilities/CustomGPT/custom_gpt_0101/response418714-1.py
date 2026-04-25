
import subprocess as sp
import os

input_dir = '/path/to/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    command = ['ls', '-lh', f'*CSV*APP*{e}.zip']
    proc_out = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    proc_out_list.append((out.decode(), err.decode()))
    print(out.decode() if out else err.decode())
