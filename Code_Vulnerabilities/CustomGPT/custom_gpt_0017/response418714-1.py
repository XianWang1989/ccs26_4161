
import subprocess as sp
import glob

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    pattern = f"{input_dir}/*CSV*APP*{e}.zip"
    matching_files = glob.glob(pattern)

    for file in matching_files:
        proc_out = sp.Popen(['ls', '-lh', file], stdout=sp.PIPE, stderr=sp.PIPE)
        proc_out_list.append(proc_out)
        stdout, stderr = proc_out.communicate()
        print(stdout.decode() if stdout else stderr.decode())
