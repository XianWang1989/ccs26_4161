
import os
import subprocess as sp

input_dir = '/path/to/your/directory'
os.chdir(input_dir)

piv_id_list = ['1000', '2000', '3000']
proc_out_list = []

for e in piv_id_list:
    pattern = f"*CSV*APP*{e}.zip"
    matching_files = [f for f in os.listdir() if fnmatch.fnmatch(f, pattern)]

    for f in matching_files:
        proc_out = sp.Popen(['ls', '-lh', f], stdout=sp.PIPE, stderr=sp.PIPE)
        output, error = proc_out.communicate()
        proc_out_list.append((output.decode(), error.decode()))
        print(f"Output for {f}: {output.decode()}")
        if error:
            print(f"Error: {error.decode()}")
