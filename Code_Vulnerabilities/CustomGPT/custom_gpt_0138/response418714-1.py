
import subprocess as sp

input_dir = '/path/to/your/directory'  # Update with your directory path
piv_id_list = [1000, 1001]  # Sample list of account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    print(output.decode())
    if error:
        print(f"Error: {error.decode()}")
