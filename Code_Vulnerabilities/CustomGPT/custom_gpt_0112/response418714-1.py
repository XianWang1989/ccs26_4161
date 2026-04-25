
import subprocess as sp
import os

# Change to the desired input directory
input_dir = 'path_to_your_directory'  # Replace with your directory path
os.chdir(input_dir)  # Change directory in Python

proc_out_list = []
piv_id_list = ['1000', '1001']  # Sample account numbers

for e in piv_id_list:
    # Construct the file pattern
    file_pattern = '*CSV*APP*{0}.zip'.format(e)
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = proc_out.communicate()

    if proc_out.returncode == 0:
        print(out.decode())
    else:
        print(f"Error: {err.decode().strip()}")
