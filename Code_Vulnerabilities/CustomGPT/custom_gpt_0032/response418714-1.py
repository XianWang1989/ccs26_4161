
import subprocess as sp
import os

# Set the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)

proc_out_list = []
piv_id_list = ['1000', '1001']  # Example account numbers

for e in piv_id_list:
    # Construct the file pattern
    file_pattern = '*CSV*APP*{0}.zip'.format(e)

    # Run the ls command
    proc_out = sp.Popen(['ls', '-lh', file_pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(f"Error: {stderr.decode().strip()}")
