
import subprocess as sp
import os

# Change the working directory
os.chdir(input_dir)

proc_out_list = []
for i, e in enumerate(piv_id_list):
    # Create the filename pattern
    filename_pattern = '*CSV*APP*{0}.zip'.format(e)

    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', filename_pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

    # Capture the output and errors
    stdout, stderr = proc_out.communicate()

    # Decode the output from bytes to string
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

    proc_out_list.append(proc_out)
