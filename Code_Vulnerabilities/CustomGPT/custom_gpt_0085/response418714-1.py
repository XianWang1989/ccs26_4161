
import subprocess as sp

input_dir = '/path/to/directory'
piv_id_list = ['1000', '1001']  # example account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True, cwd=input_dir)
    stdout, stderr = proc_out.communicate()
    proc_out_list.append(stdout.strip())  # Collect the output
    if stderr:
        print(f"Error: {stderr.strip()}")  # Print any errors

# Print the results
for output in proc_out_list:
    print(output)
