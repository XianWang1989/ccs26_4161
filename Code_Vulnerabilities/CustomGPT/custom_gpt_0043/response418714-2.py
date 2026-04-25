
import os

input_dir = '/path/to/your/directory'  # Replace with your directory
piv_id_list = ['1000', '2000']  # Sample account numbers

for e in piv_id_list:
    # Construct the filename pattern
    pattern = f'CSV*APP*{e}.zip'
    found_files = [f for f in os.listdir(input_dir) if fnmatch.fnmatch(f, pattern)]

    if found_files:
        for filename in found_files:
            print(os.path.join(input_dir, filename))  # Print full path
    else:
        print(f'No files matching {pattern} found in {input_dir}.')
