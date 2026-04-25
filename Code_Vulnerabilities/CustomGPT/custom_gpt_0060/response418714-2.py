
import subprocess as sp

input_dir = '/your/directory/here'  # Set your directory path
piv_id_list = ['1000', '1001']  # List of account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
