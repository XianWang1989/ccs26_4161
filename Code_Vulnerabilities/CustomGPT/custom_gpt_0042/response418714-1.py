
import subprocess as sp

input_dir = '/path/to/your/directory'  # Change this to your actual directory
piv_id_list = ['1000', '1001']  # Replace with your actual account numbers

proc_out_list = []

# Change to the input directory
sp.chdir(input_dir)

for e in piv_id_list:
    # Use the shell to expand the wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())  # Display the output
    else:
        print(stderr.decode())   # Display the error
