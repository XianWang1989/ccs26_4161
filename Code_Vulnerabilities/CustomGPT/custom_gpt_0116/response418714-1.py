
import subprocess as sp
import os

input_dir = '/your/input/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Sample list of account numbers
proc_out_list = []

# Change the working directory to input_dir
os.chdir(input_dir)

for e in piv_id_list:
    # Run ls with shell=True to enable wildcard expansion
    proc_out = sp.Popen(f'ls -lh *CSV*APP*{e}.zip', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Get output and error messages
    proc_out_list.append(stdout.decode())

    if proc_out.returncode != 0:
        print(f"Error: {stderr.decode()}")
    else:
        print(stdout.decode())
