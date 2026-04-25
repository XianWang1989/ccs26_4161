
import subprocess as sp
import os

input_dir = 'your_directory'  # Set your input directory here
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

os.chdir(input_dir)
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()

    if proc_out.returncode == 0:
        print(f'Output for {e}:\n{output.decode()}')
    else:
        print(f'Error for {e}:\n{error.decode()}')
