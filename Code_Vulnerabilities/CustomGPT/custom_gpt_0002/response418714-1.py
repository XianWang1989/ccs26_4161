
import subprocess as sp

input_dir = "your_directory_path"  # Replace with your actual directory
piv_id_list = [1000, 1001, 1002]  # Example list of account numbers
proc_out_list = []

# Change the working directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    proc_out_list.append(output.decode('utf-8'))  # Capture output
    if error:
        print(f"Error: {error.decode('utf-8')}")
    else:
        print(output.decode('utf-8'))
