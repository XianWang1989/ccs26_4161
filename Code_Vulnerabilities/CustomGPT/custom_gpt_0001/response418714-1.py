
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.call(command, shell=True)
