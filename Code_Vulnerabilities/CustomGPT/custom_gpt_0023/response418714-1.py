
import subprocess as sp
import glob

# Change to the target directory
input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers

# Use glob to find files
proc_out_list = []
for e in piv_id_list:
    pattern = f"{input_dir}/CSV*APP*{e}.zip"
    files = glob.glob(pattern)

    if files:
        # Run ls for found files
        for file in files:
            proc_out = sp.Popen(['ls', '-lh', file])
            proc_out_list.append(proc_out)
            print(f"Running ls on: {file}")
    else:
        print(f"No files found for pattern: {pattern}")
