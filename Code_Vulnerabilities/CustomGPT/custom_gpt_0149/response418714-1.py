
import subprocess as sp
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the working directory for the subprocess call
for e in piv_id_list:
    # Construct the filename pattern
    filename_pattern = f'*CSV*APP*{e}.zip'

    # Using shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', filename_pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and error
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

    proc_out_list.append(proc_out)
