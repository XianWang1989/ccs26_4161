
import subprocess as sp
import os
import glob

# Set the input directory
input_dir = '/path/to/your/directory'
os.chdir(input_dir)  # Change to your desired directory

proc_out_list = []
for e in piv_id_list:
    # Use glob to find matching files
    pattern = f'*CSV*APP*{e}.zip'
    matching_files = glob.glob(pattern)  # List all matching files

    if matching_files:  # Check if there are matching files
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            stdout, stderr = proc_out.communicate()
            print(stdout.decode().strip())
            if stderr:
                print(stderr.decode().strip())
    else:
        print(f'No files found for: {pattern}')
