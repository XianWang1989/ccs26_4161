
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Sample account numbers

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)
    print(proc_out.stdout)  # Print the output
