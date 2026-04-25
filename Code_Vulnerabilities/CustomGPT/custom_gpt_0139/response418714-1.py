
import subprocess as sp

input_dir = "/path/to/directory"  # Change this to your actual directory
piv_id_list = ['1000', '2000', '3000']  # Sample list of account numbers
proc_out_list = []

# Run the command with shell=True
for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Get output and error
    proc_out_list.append((out.decode(), err.decode()))  # Decode bytes to string
    print("Output:", out.decode())
    print("Error:", err.decode())
