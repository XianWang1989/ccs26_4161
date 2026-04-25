
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory here
piv_id_list = [1000, 1001]  # Example account numbers
proc_out_list = []

# Change directory using os.chdir to ensure current working directory is set
import os
os.chdir(input_dir)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())  # Print successful output
    else:
        print(stderr.decode())   # Print error message
