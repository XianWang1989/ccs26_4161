
import subprocess as sp
import glob
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '2000']  # example account numbers
proc_out_list = []

# Change to desired working directory
os.chdir(input_dir)

for e in piv_id_list:
    pattern = f"*CSV*APP*{e}.zip"
    files = glob.glob(pattern)  # Get list of matching files

    for file in files:
        proc_out = sp.Popen(['ls', '-lh', file])
        proc_out_list.append(proc_out)
        print(proc_out)
