
import subprocess as sp

input_dir = '/path/to/your/dir'  # Set your input directory
piv_id_list = ['1000', '1001']    # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    command = f"ls -lh *CSV*APP*{e}.zip"
    proc_out = sp.Popen(command, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)

    out, err = proc_out.communicate()
    if proc_out.returncode == 0:
        print(out.decode())
    else:
        print(err.decode())
