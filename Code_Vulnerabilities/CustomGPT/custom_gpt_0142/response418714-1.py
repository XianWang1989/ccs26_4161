
import subprocess as sp

# Sample input_dir and piv_id_list for demonstration purposes
input_dir = '/path/to/directory'  # Set your target directory
piv_id_list = ['1000', '1001']     # Sample account numbers
proc_out_list = []

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

# Run the ls command for each account number
for e in piv_id_list:
    command = "ls -lh *CSV*APP*{0}.zip".format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Get the output and errors
    proc_out_list.append(out)  # Store the output
    if err:  # Check for and print errors
        print(f"Error: {err.decode()}")
    else:
        print(out.decode())  # Print the output
