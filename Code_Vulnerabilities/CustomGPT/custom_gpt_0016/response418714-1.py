
import subprocess as sp

input_dir = '/path/to/directory'  # Make sure to specify your directory.
piv_id_list = ['1000', '1001']  # Example account numbers.
proc_out_list = []

# Change directory to input_dir
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    proc_out = sp.Popen(f'ls -lh *CSV*APP*{e}.zip', shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Collect output and error messages
    proc_out_list.append(out.decode())  # Append the output to the list
    if err:
        print(f"Error: {err.decode()}")
    else:
        print(out.decode())
