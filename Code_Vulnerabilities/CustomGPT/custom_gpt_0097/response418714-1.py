
import subprocess as sp

input_dir = 'your_directory'  # Replace with your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))
    print(out.decode('utf-8'), err.decode('utf-8'))
