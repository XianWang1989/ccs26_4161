
import subprocess as sp

input_dir = '/path/to/directory'  # Set your directory path here
piv_id_list = [1000, 1001, 1002]   # Example list of account numbers
proc_out_list = []

# Change the current working directory
# Use the cwd parameter in subprocess to stay in the desired directory
for i, e in enumerate(piv_id_list):
    cmd = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(cmd, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture the output and error

    # Print the output
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
