
import subprocess as sp

input_dir = '/path/to/your/directory'  # Change to your directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change directory using shell command
sp.call(['cd', input_dir], shell=True)  # Note: shell=True for `cd` won't affect current process

# Iterate through account numbers
for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output

    if out:
        print(out.decode())  # Print the output if there are files
    if err:
        print(f"Error: {err.decode()}")  # Print any errors
