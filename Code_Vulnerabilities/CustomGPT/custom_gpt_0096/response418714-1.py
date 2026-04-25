
import subprocess as sp

# Set your input directory and list of account numbers
input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001', '1002']  # Example account numbers

proc_out_list = []

for e in piv_id_list:
    # Construct the pattern for the files you want to list
    pattern = '*CSV*APP*{0}.zip'.format(e)
    # Run the 'ls' command in the specified directory
    proc_out = sp.Popen(['ls', '-lh', pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture output and errors

    if stdout:
        print(stdout.decode())  # Print the output from ls
    if stderr:
        print(stderr.decode())  # Print any errors

