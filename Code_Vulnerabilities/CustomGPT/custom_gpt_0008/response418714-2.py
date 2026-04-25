
import os
import subprocess as sp

input_dir = '/your/directory/path'  # Your directory
piv_id_list = ['1000', '1001']
proc_out_list = []

# Change to the input directory
os.chdir(input_dir)

for e in piv_id_list:
    search_pattern = f'*CSV*APP*{e}.zip'
    matches = [f for f in os.listdir('.') if fnmatch.fnmatch(f, search_pattern)]

    if matches:
        for match in matches:
            proc_out = sp.Popen(['ls', '-lh', match], stdout=sp.PIPE, stderr=sp.PIPE)
            out, err = proc_out.communicate()
            if proc_out.returncode == 0:
                print(out.decode())
            else:
                print(err.decode())
    else:
        print(f"No files found matching pattern: {search_pattern}")
