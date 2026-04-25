
import subprocess as sp

# Use 'ls' with shell=True to enable wildcard expansion
for i, e in enumerate(piv_id_list):
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    proc_out_list.append(proc_out)

    # Capture the output and error
    stdout, stderr = proc_out.communicate()

    # Decode the output from bytes to string
    print(stdout.decode('utf-8') if stdout else stderr.decode('utf-8'))
