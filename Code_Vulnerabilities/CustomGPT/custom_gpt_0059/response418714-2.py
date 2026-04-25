
import subprocess as sp
import glob
import os

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Sample account numbers

for e in piv_id_list:
    # Expand the wildcard using glob
    files = glob.glob(os.path.join(input_dir, f'*CSV*APP*{e}.zip'))
    for file in files:
        proc_out = sp.run(['ls', '-lh', file], capture_output=True, text=True)
        print(proc_out.stdout)  # Print the output
