
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Replace with your actual directory path
piv_id_list = ['1000', '1001', '1002']  # Example account numbers

# Change the directory
os.chdir(input_dir)

proc_out_list = []
for e in piv_id_list:
    cmd = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(f"Error: {stderr.decode()}")
