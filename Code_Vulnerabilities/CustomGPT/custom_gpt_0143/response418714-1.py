
import subprocess as sp
import glob

input_dir = 'your_directory_path'  # Replace with your directory path
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Construct the filename pattern
    pattern = f"{input_dir}/*CSV*APP*{e}.zip"
    # Use glob to find the matching files
    files = glob.glob(pattern)

    for file in files:
        # Run the ls command on each found file
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = proc_out.communicate()
        proc_out_list.append((out.decode(), err.decode()))
        print(out.decode(), err.decode())
