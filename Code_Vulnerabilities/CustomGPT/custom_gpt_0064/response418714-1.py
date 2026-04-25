
import subprocess as sp

input_dir = "/path/to/your/input_dir"  # Set your directory path here
piv_id_list = ["1000", "1001", "1002"]  # Example account numbers
proc_out_list = []

# Change to the specified directory
sp.call(['cd', input_dir], shell=True)

# Run ls command for each account number
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, text=True, cwd=input_dir)
    output, errors = proc_out.communicate()
    proc_out_list.append(output)
    if errors:
        print(f"Error: {errors}")
    else:
        print(output)
