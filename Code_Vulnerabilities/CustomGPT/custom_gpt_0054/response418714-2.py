
import subprocess as sp
from glob import glob

input_dir = "/path/to/directory"  # Replace with your actual directory
piv_id_list = ["1000", "1001"]  # Replace with your actual list of identifiers
proc_out_list = []

for e in piv_id_list:
    pattern = f"{input_dir}/*CSV*APP*{e}.zip"
    matching_files = glob(pattern)  # Get the list of matching files

    for file in matching_files:
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = proc_out.communicate()

        if proc_out.returncode == 0:
            print(out.decode())
        else:
            print(err.decode())
