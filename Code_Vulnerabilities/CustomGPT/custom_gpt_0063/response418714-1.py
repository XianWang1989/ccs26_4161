
import subprocess as sp

input_dir = 'your/input/directory'  # Change this to your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change directory to input_dir
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to allow for wildcard expansion
    command = "ls -lh *CSV*APP*{0}.zip".format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())  # Print the output if the command was successful
    else:
        print(f"Error: {stderr.decode()}")  # Print error message if failed
