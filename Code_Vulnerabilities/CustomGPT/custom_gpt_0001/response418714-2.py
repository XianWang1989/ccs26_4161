
import subprocess as sp
import glob
import os

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers

for e in piv_id_list:
    pattern = os.path.join(input_dir, f'*CSV*APP*{e}.zip')
    files = glob.glob(pattern)

    for file in files:
        proc_out = sp.call(['ls', '-lh', file])
