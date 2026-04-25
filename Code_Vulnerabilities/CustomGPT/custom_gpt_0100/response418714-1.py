
import subprocess as sp
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the file name pattern
    file_pattern = '*CSV*APP*{0}.zip'.format(e)

    # Use the shell=True to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    if proc_out.returncode == 0:
        print(out.decode())
    else:
        print(f"Error: {err.decode()}")
