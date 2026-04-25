
import subprocess as sp
import os

input_dir = 'your_directory_path_here'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example list of account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    print(output.decode())
    if error:
        print("Error:", error.decode())
