
import subprocess as sp

input_dir = '/path/to/your/directory'
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # You can run the command in the directory using shell=True
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    proc_out_list.append(output)
    if error:
        print("Error:", error.decode())
    else:
        print("Output:", output.decode())
