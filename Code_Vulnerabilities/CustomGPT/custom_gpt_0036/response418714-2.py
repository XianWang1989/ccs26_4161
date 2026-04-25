
import os
import glob

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Make sure to change the working directory
os.chdir(input_dir)

for e in piv_id_list:
    pattern = '*CSV*APP*{0}.zip'.format(e)
    matched_files = glob.glob(pattern)  # Use glob to find matching files
    if matched_files:
        for file in matched_files:
            print(file)  # Print each matched file
            proc_out_list.append(file)
    else:
        print('No matching files for pattern:', pattern)
