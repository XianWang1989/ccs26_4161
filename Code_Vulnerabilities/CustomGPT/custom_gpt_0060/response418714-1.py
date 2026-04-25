
import os

input_dir = '/your/directory/here'  # Set your directory path
piv_id_list = ['1000', '1001']  # List of account numbers
proc_out_list = []

for e in piv_id_list:
    search_pattern = f"*CSV*APP*{e}.zip"
    matches = [f for f in os.listdir(input_dir) if fnmatch.fnmatch(f, search_pattern)]
    if matches:
        for match in matches:
            print(f"Found file: {match}")
    else:
        print(f"No files found matching pattern: {search_pattern}")
