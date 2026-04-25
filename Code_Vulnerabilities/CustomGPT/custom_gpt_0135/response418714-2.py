
import os
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # Construct the file path
    file_path_pattern = os.path.join(input_dir, f"*CSV*APP*{e}.zip")
    proc_out = sp.Popen(['ls', '-lh', file_path_pattern], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    proc_out_list.append(output)
    if error:
        print("Error:", error.decode())
    else:
        print("Output:", output.decode())
