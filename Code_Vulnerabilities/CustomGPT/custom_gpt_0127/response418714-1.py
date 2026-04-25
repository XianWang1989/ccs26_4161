
import subprocess as sp
import shlex

# Change directory first
sp.call(['cd', input_dir], shell=True)

proc_out_list = []
for e in piv_id_list:
    # Construct the shell command as a string
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    # Use shlex to handle the command string
    proc_out = sp.Popen(shlex.split(command), stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc_out.communicate()

    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())

proc_out_list.append(proc_out)
