
import os
import subprocess as sp

# Change to the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)

# Sample pivot ID list
piv_id_list = ['1000', '1001', '1002']
proc_out_list = []

for e in piv_id_list:
    file_pattern = f'*CSV*APP*{e}.zip'
    # Use the shell=True argument to allow wildcard expansion
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    stdout, stderr = proc_out.communicate()

    # Store the output and print it
    proc_out_list.append(stdout.decode() if stdout else stderr.decode())
    print(proc_out_list[-1])  # Print the latest output

