
import subprocess as sp
import os

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change the current working directory
os.chdir(input_dir)

for e in piv_id_list:
    file_pattern = f'*CSV*APP*{e}.zip'
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Wait for the command to complete and capture output
    proc_out_list.append((stdout.decode(), stderr.decode()))  # Decode and store the output

# Print the outputs
for output, error in proc_out_list:
    if output:
        print("Output:\n", output)
    if error:
        print("Error:\n", error)
