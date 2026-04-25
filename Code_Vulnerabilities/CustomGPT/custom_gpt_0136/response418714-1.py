
import subprocess as sp

# Assuming input_dir is defined and piv_id_list is your list of account numbers
input_dir = '/path/to/your/directory'  # Update with your actual directory

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    proc_out_list, proc_err_list = proc_out.communicate()

    # Print the output and error messages, if any
    print(proc_out_list.decode())
    if proc_err_list:
        print(proc_err_list.decode())
