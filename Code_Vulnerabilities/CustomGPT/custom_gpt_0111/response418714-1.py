
import subprocess as sp

input_dir = '/path/to/your/directory'  # set your directory path
piv_id_list = ['1000', '1001', '1002']  # sample account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True) 

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    # Append output to the list
    proc_out_list.append(proc_out.stdout)

    # Print results
    if proc_out.returncode == 0:
        print(proc_out.stdout)
    else:
        print(f"Error: {proc_out.stderr}")
