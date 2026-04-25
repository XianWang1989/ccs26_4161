
import subprocess as sp
import os

input_dir = 'path/to/your/directory'  # Update this to your actual input directory
piv_id_list = ['1000', '2000']  # Example account numbers
proc_out_list = []

# Change to the target directory
os.chdir(input_dir)

for e in piv_id_list:
    # Construct the pattern for the file search
    pattern = '*CSV*APP*{0}.zip'.format(e)

    # Use glob to expand the wildcard pattern
    matching_files = glob.glob(pattern)

    if matching_files:
        for file in matching_files:
            proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
            proc_out_list.append(proc_out)
            output, errors = proc_out.communicate()
            print(output.decode('utf-8'))
    else:
        print(f"No files found matching pattern: {pattern}")
