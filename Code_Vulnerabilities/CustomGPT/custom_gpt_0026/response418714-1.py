
import subprocess as sp
import glob
import os

input_dir = '/path/to/your/directory'  # Specify your directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the working directory
os.chdir(input_dir)

for i, e in enumerate(piv_id_list):
    # Use glob to find files matching the pattern
    file_pattern = f'*CSV*APP*{e}.zip'
    matching_files = glob.glob(file_pattern)

    if matching_files:  # Check if any files were found
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = proc_out.communicate()  # Capture output and errors
            proc_out_list.append(out.decode() if out else err.decode())
            print(out.decode() if out else err.decode())
    else:
        print(f"No files found matching: {file_pattern}")
