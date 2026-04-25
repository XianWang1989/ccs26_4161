
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    proc_out_list.append(proc_out)
    stdout, stderr = proc_out.communicate()
    print(stdout.decode() if stdout else stderr.decode())
