
import subprocess as sp
import shlex
import os

# Define your input directory
input_dir = 'path/to/your/directory'
os.chdir(input_dir)  # Change the current working directory

proc_out_list = []
for e in piv_id_list:
    # Create the command with wildcards using shlex
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(shlex.split(command), stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture output and error

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

    proc_out_list.append(proc_out)

