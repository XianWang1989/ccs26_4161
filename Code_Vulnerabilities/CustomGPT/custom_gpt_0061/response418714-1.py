
import subprocess as sp

input_dir = '/path/to/your/directory'  # specify the directory
piv_id_list = ['1000', '1001', '1002']  # sample account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    proc_out_list.append(out)

    if err:
        print(f"Error: {err.decode().strip()}")
    else:
        print(out.decode().strip())
