
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Replace with your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change to the desired directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the filename pattern
    filename_pattern = f'*CSV*APP*{e}.zip'

    # Execute `ls` with shell expansion
    proc_out = sp.Popen(['ls', '-lh', filename_pattern], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    output, error = proc_out.communicate()

    if output:
        print(output.decode())
    if error:
        print(error.decode())
