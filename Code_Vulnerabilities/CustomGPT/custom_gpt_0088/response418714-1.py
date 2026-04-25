
import subprocess as sp

input_dir = "your/input/directory"  # replace with your input directory
piv_id_list = [1000, 1001]  # example account numbers
proc_out_list = []

# Change the working directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()
    proc_out_list.append(out.decode())
    if err:
        print(f"Error: {err.decode()}")

# Print the output of the ls command
for output in proc_out_list:
    print(output)
