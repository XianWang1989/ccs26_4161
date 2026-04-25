
import subprocess as sp

# Use 'cd' in the command instead of a separate call
input_dir = "/path/to/your/directory"
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change directory using subprocess with shell=True
for e in piv_id_list:
    command = f"ls -lh *CSV*APP*{e}.zip"
    proc_out = sp.Popen(command, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    if out:
        print(out.decode())
    if err:
        print(err.decode())
