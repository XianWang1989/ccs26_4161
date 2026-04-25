
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Run `ls` in the specified directory
for e in piv_id_list:
    proc_out = sp.Popen(['ls', '-lh', f'{input_dir}/*CSV*APP*{e}.zip'], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture output and error
    if stdout:
        print(stdout.decode())  # Print standard output
    if stderr:
        print(stderr.decode())  # Print errors
