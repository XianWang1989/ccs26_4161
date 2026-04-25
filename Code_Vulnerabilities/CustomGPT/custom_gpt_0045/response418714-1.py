
import subprocess as sp

# Change working directory
input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '2000']  # example account numbers
proc_out_list = []

# Note: Using Shell=True can introduce security risks with untrusted input
for e in piv_id_list:
    command = f"ls -lh *CSV*APP*{e}.zip"
    proc_out = sp.Popen(command, shell=True, cwd=input_dir)
    proc_out_list.append(proc_out)
    print(proc_out)
