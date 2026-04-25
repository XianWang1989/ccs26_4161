
import subprocess as sp

input_dir = '/path/to/directory'  # update to your directory
piv_id_list = ['1000', '1001', '1002']  # example account numbers
proc_out_list = []

# Change to the specified directory
sp.run(f'cd {input_dir}', shell=True)

for e in piv_id_list:
    # Using shell=True for wildcard expansion
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    # Print the command output
    print(proc_out.stdout)
    if proc_out.stderr:
        print("Error:", proc_out.stderr)

    proc_out_list.append(proc_out)
