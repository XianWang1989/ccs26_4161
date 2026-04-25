
import subprocess as sp

input_dir = '/path/to/directory'  # Set your directory path
piv_id_list = ['1000']  # Example list of account numbers
proc_out_list = []

# Change to the directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    proc_out_list.append(proc_out)
    output, errors = proc_out.communicate()
    print(f"Output:\n{output.decode()}")
    if errors:
        print(f"Errors:\n{errors.decode()}")
