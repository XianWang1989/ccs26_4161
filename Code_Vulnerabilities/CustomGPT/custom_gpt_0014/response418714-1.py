
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the target directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Construct the complete ls command
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    out, err = proc_out.communicate()

    if out:
        print(out.decode())
    if err:
        print(err.decode())
