
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your directory path
piv_id_list = ['1000', '2000']  # Example IDs
proc_out_list = []

for e in piv_id_list:
    proc_out = sp.Popen(['ls', '-lh', '*CSV*APP*{0}.zip'.format(e)], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    output, errors = proc_out.communicate()  # Capture the output and errors
    proc_out_list.append((output, errors))  # Append the output and errors to the list
    print(output.decode() if output else errors.decode())  # Print the output or errors
