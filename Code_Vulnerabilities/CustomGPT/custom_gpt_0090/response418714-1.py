
import subprocess as sp

input_dir = '/path/to/your/directory'  # Update this path
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)
    proc_out_list.append(proc_out.stdout)
    print(proc_out.stdout)
