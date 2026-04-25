
import subprocess as sp
import os
import glob

input_dir = '/path/to/your/directory'  # Update this with your actual path
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change the directory for the subprocess calls
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to find matching files
    pattern = f'*CSV*APP*{e}.zip'
    matching_files = glob.glob(pattern)

    if matching_files:
        for file in matching_files:
            # Call ls on each matched file
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            stdout, stderr = proc_out.communicate()
            print(stdout.decode() if stdout else stderr.decode())
            proc_out_list.append(proc_out)
    else:
        print(f'No files found matching pattern: {pattern}')
