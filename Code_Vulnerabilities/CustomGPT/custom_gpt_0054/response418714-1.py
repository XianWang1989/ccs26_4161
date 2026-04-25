
import subprocess as sp

input_dir = "/path/to/directory"  # Replace with your actual directory
piv_id_list = ["1000", "1001"]  # Replace with your actual list of identifiers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    # Capture the output and error
    if proc_out.returncode == 0:
        print(out.decode())
    else:
        print(err.decode())
