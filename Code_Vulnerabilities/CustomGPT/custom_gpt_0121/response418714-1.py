
import subprocess as sp

# Change to the input directory
input_dir = '/path/to/your/directory'  # Make sure to set your directory
sp.call(['cd', input_dir], shell=True)

piv_id_list = ['1000', '2000', '3000']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    proc_out_list.append((output.decode(), error.decode()))
    print(f"Output for {e}: {output.decode()}")
    if error:
        print(f"Error: {error.decode()}")
