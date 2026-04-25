
import subprocess as sp
import os

# Make sure to change to the desired directory
os.chdir(input_dir)

# Initialize an empty list to store process outputs
proc_out_list = []

for e in piv_id_list:
    # Create the search pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)

    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

    # Capture the output and errors
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())
        proc_out_list.append(stderr.decode())
