
import os
import subprocess as sp
import glob

input_dir = '/path/to/your/directory'  # Change this to your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to find matching files
    pattern = '*CSV*APP*{0}.zip'.format(e)
    matching_files = glob.glob(pattern)

    if matching_files:
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            proc_out_list.append(proc_out)
            out, err = proc_out.communicate()
            print(out.decode() if out else err.decode())
    else:
        print(f"No files found for pattern: {pattern}")
