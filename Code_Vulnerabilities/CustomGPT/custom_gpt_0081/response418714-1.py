
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your directory path here
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True, cwd=input_dir)
    out, err = proc_out.communicate()

    if out:
        print("Output:\n", out.decode())
    if err:
        print("Error:\n", err.decode())

    proc_out_list.append(proc_out)
