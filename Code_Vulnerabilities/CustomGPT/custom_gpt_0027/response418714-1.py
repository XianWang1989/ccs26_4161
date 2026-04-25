
import subprocess as sp
import os

input_dir = '/path/to/your/directory'  # Set your directory path
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to the target directory
os.chdir(input_dir)

# Iterate over account numbers and run the ls command
for e in piv_id_list:
    file_pattern = '*CSV*APP*{0}.zip'.format(e)
    # Use glob to expand the file pattern
    matched_files = sp.getoutput(f'ls -lh {file_pattern}')
    if matched_files:
        proc_out_list.append(matched_files)
    else:
        proc_out_list.append(f'No files found for {file_pattern}')
    print(matched_files)

# Optionally, print proc_out_list if needed
print(proc_out_list)
