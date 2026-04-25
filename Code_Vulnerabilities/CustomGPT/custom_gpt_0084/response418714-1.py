
import subprocess as sp

input_dir = 'your_directory_path'  # Specify your input directory
piv_id_list = ['1000', '1001', '1002']  # Example account numbers
proc_out_list = []

# Change to input directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture output and errors
    proc_out_list.append(out.decode() if out else err.decode())  # Store the output or error

# Print results
for output in proc_out_list:
    print(output)
