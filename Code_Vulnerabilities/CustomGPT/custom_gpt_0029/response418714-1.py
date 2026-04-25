
import subprocess as sp
import os

# Change to the directory containing the files
os.chdir(input_dir)

proc_out_list = []
for e in piv_id_list:
    # Construct the file pattern
    pattern = f"*CSV*APP*{e}.zip"

    # Use shell=True to allow shell features like wildcard expansion
    proc_out = sp.Popen(f'ls -lh {pattern}', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture the output and errors
    stdout, stderr = proc_out.communicate()

    # Print the output or error
    print(stdout.decode() if stdout else stderr.decode())

    proc_out_list.append(proc_out)
