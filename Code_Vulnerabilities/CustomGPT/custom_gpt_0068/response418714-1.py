
import subprocess as sp

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

# Assuming `input_dir` is defined and `piv_id_list` is populated
proc_out_list = []
for e in piv_id_list:
    cmd = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()  # Capture output and error
    proc_out_list.append(stdout)

    if stdout:
        print(stdout.decode('utf-8'))  # Print the output from the command
    if stderr:
        print(stderr.decode('utf-8'))  # Print any errors
