
import os

input_dir = '/path/to/your/directory'  # Specify your input directory here
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Iterate over the account numbers
for e in piv_id_list:
    # Construct the filename based on the input
    file_name = f"*CSV*APP*{e}.zip"
    # List all files in the input directory
    files = os.listdir(input_dir)
    # Filter files matching the pattern
    matching_files = [f for f in files if fnmatch.fnmatch(f, file_name)]

    if matching_files:
        print(f"Matching files for {e}: {matching_files}")
    else:
        print(f"No matching files for {e}.")
