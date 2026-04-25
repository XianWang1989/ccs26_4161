
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory.
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers.
proc_out_list = []

# Change the working directory
sp.call(['cd', input_dir], shell=True)

# Loop through your account numbers
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = proc_out.communicate()  # Capture output and error
    proc_out_list.append(output.decode() if output else None)

    if error:
        print(f"Error: {error.decode()}")
    else:
        print(output.decode())
