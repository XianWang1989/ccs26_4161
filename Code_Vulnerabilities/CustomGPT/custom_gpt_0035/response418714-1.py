
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set the correct path
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    cmd = f'ls -lh *CSV*APP*{e}.zip'
    # Execute the command in the specified directory
    proc_out = sp.Popen(cmd, cwd=input_dir, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    proc_out_list.append(out)

    if proc_out.returncode == 0:
        print(out.decode())  # Print successful output
    else:
        print(f"Error: {err.decode()}")  # Print error message
