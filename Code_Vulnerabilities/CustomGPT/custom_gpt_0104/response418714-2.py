
import os
import glob

input_dir = '/path/to/directory'  # Set your input directory path
piv_id_list = ['1000', '1001', '1002']  # Sample account numbers
proc_out_list = []

# Change the current working directory to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    # Use glob to match the files with the pattern
    pattern = f'*CSV*APP*{e}.zip'
    found_files = glob.glob(pattern)

    if found_files:
        for file in found_files:
            print(f"Found: {file}")
    else:
        print(f"No files found for pattern: {pattern}")
