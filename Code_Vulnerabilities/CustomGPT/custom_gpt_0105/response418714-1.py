
import subprocess as sp
import os

# Change to the desired directory
os.chdir(input_dir)

# List to store subprocess output
proc_out_list = []

for e in piv_id_list:
    # Build the file pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())
