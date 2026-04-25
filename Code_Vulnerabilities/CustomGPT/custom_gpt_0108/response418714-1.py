
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Replace with your actual IDs
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()  # Capture output and error
    if output:
        print(f"Output for {e}:\n{output.decode()}")
    if error:
        print(f"Error for {e}:\n{error.decode()}")
