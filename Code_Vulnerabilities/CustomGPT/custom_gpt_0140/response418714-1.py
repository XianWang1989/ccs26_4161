
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '2000']  # Replace with your actual IDs
proc_out_list = []

# Change to the target directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to expand the wildcard
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, errors = proc_out.communicate()

    proc_out_list.append(output.decode())

    if errors:
        print(f"Error: {errors.decode()}")
    else:
        print(output.decode())

# Print the results
for result in proc_out_list:
    print(result)
