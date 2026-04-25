
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to the desired directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use the shell=True option to enable wildcard expansion
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    try:
        proc_out = sp.check_output(command, shell=True, text=True)
        proc_out_list.append(proc_out)
        print(proc_out)
    except sp.CalledProcessError as e:
        print(f"Error: {e.output}")

# Display the results
for result in proc_out_list:
    print(result)
