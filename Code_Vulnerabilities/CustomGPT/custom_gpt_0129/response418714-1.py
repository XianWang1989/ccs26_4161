
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Example account numbers

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'  # Combining the path and the pattern
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Get the output and any errors
    print(stdout.decode() if stdout else stderr.decode())
