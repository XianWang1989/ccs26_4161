
import subprocess as sp

input_dir = "/path/to/your/directory"  # Specify your directory
piv_id_list = ["1000", "1001"]  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()

    if output:
        print(output.decode())  # Print the file listings
    if error:
        print(error.decode())  # Print any error messages
