
import subprocess as sp

input_dir = '/path/to/your/directory'  # Make sure to set your input directory
piv_id_list = ['1000', '1001']  # Example list of account numbers
proc_out_list = []

# Change the directory first
sp.call(['cd', input_dir], shell=True)

# Iterate through the ids and run the command
for i, e in enumerate(piv_id_list):
    command = "ls -lh *CSV*APP*{0}.zip".format(e)  # Prepare the command string
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)  # Execute command
    stdout, stderr = proc_out.communicate()  # Capture the output and errors
    proc_out_list.append(stdout.decode())  # Store the output
    if stderr:
        print(f"Error: {stderr.decode()}")  # Print any errors
    else:
        print(stdout.decode())  # Print the output
