
import subprocess as sp

input_dir = '/path/to/directory'  # Change this to your directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

for i, e in enumerate(piv_id_list):
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    if proc_out.returncode == 0:
        proc_out_list.append(proc_out.stdout)
        print(proc_out.stdout)
    else:
        print(f'Error: {proc_out.stderr}')
