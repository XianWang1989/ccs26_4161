
import subprocess as sp

input_dir = "/path/to/your/directory"  # Change this to your directory
piv_id_list = ["1000", "1001"]  # Sample account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use the shell to expand wildcards
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, cwd=input_dir)
    output, error = proc_out.communicate()

    # Decode bytes to string and print
    if output:
        print(output.decode())
    if error:
        print("Error:", error.decode())
