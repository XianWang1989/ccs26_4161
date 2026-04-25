import subprocess as sp
import os

input_dir = "/your/path/here"
piv_id_list = ["1000", "2000"]  # Replace with your actual list

os.chdir(input_dir)  # Change working directory for current Python process
proc_out_list = []

for e in piv_id_list:
    pattern = f"*CSV*APP*{e}.zip"
    cmd = f"ls -lh {pattern}"
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    if out:
        print(out.decode())
    if err:
        print(err.decode())
    proc_out_list.append(proc_out)
