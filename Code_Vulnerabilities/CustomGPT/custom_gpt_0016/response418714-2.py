
import subprocess as sp
import glob
import os

input_dir = '/path/to/directory'  # Make sure to specify your directory.
piv_id_list = ['1000', '1001']  # Example account numbers.
proc_out_list = []

# Change to the target directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to find files matching the pattern
    files = glob.glob(f'*CSV*APP*{e}.zip')
    for file in files:
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = proc_out.communicate()  # Collect output and error messages
        proc_out_list.append(out.decode())  # Append output to the list
        if err:
            print(f"Error: {err.decode()}")
        else:
            print(out.decode())
