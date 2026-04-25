
import subprocess as sp

input_dir = '/path/to/directory'  # Replace with your directory path
piv_id_list = ['1000', '1001']  # Sample list of account numbers
proc_out_list = []  # To store the process outputs

# Change directory to input_dir using subprocess call
sp.call(['cd', input_dir], shell=True)

# Iterate over the list of piv_id
for e in piv_id_list:
    # Construct the command string
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)

    # Execute the command in the shell
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Get the output and errors
    output, error = proc_out.communicate()

    # Append the output if you need to keep track or print it
    proc_out_list.append(output.decode())

    # Print the standard output or error if any
    if output:
        print("Output:\n", output.decode())
    if error:
        print("Error:\n", error.decode())
