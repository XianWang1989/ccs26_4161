
import subprocess as sp
import os

# Change to the desired input directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the filename pattern
    pattern = '*CSV*APP*{0}.zip'.format(e)

    # Run the ls command
    proc_out = sp.Popen(['ls', '-lh', pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if proc_out.returncode == 0:
        print(stdout.decode())
    else:
        print(f"Error: {stderr.decode()}")
