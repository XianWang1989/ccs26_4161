
import subprocess as sp

input_dir = '/path/to/your/directory'  # Update this to your target directory
piv_id_list = ['1000', '1001']  # Example account numbers

# Change to the input_dir
sp.call(['cd', input_dir], shell=True)

proc_out_list = []
for e in piv_id_list:
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True, cwd=input_dir)

    stdout, stderr = proc_out.communicate()  # Capture output and errors
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
    proc_out_list.append(proc_out)
