
import subprocess as sp
import os

# Change to the desired directory
os.chdir(input_dir)

proc_out_list = []
for e in piv_id_list:
    filename_pattern = '*CSV*APP*{0}.zip'.format(e)
    # Use the shell=True argument to allow wildcard expansion
    proc_out = sp.Popen(f'ls -lh {filename_pattern}', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and errors
    proc_out_list.append(out.decode())  # Decode the output from bytes to string

    if err:
        print(f"Error: {err.decode().strip()}")
    else:
        print(out.decode().strip())

# Print the results
for output in proc_out_list:
    print(output)
