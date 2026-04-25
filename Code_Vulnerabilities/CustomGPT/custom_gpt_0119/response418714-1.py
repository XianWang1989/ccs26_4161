
import subprocess as sp
import os

# Change to the desired directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)

# List of account numbers
piv_id_list = ['1000', '1001', '1002']  # Example list
proc_out_list = []

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(f'ls -lh *CSV*APP*{e}.zip', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and error
    proc_out_list.append(out.decode().strip())  # Decode and strip output
    if err:
        print(f'Error: {err.decode().strip()}')
    else:
        print(out.decode().strip())

# Print results
for result in proc_out_list:
    print(result)
