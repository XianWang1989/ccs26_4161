
import subprocess as sp

input_dir = 'your/directory/path'  # Replace with your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)
    proc_out_list.append(proc_out)

    if proc_out.returncode == 0:
        print(proc_out.stdout)
    else:
        print(proc_out.stderr)
