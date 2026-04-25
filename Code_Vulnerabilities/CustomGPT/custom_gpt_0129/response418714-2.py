
import subprocess as sp
import glob
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Example account numbers

for e in piv_id_list:
    # Forming the pattern accordingly
    pattern = os.path.join(input_dir, f'*CSV*APP*{e}.zip')
    matching_files = glob.glob(pattern)  # Get files matching the pattern

    for file in matching_files:
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = proc_out.communicate()  # Get the output and any errors
        print(stdout.decode() if stdout else stderr.decode())
