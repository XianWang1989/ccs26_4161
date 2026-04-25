
import subprocess as sp
import os

input_dir = '/your/directory/path'  # Set your input directory here
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the desired directory
os.chdir(input_dir)

for e in piv_id_list:
    cmd = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    if proc_out.returncode == 0:
        print(out.decode())
    else:
        print(err.decode())
