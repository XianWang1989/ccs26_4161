
import subprocess as sp
import glob
import os

input_dir = '/path/to/directory'  # Change this to your input directory
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

# Change directory (using os)
os.chdir(input_dir)

for e in piv_id_list:
    pattern = '*CSV*APP*{0}.zip'.format(e)
    matching_files = glob.glob(pattern)

    if matching_files:
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = proc_out.communicate()

            if proc_out.returncode == 0:
                print(output.decode())
            else:
                print(f"Error: {error.decode()}")
    else:
        print(f"No matching files for pattern: {pattern}")
