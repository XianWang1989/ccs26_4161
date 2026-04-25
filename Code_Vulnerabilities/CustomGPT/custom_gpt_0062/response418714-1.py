
import subprocess as sp

# Change to the desired directory
sp.call(['cd', input_dir], shell=True)

proc_out_list = []
for e in piv_id_list:
    # Run ls command with wildcard through the shell
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and errors
    proc_out_list.append(out)

    if out:
        print(out.decode())  # Print the standard output
    if err:
        print(err.decode())  # Print the errors if any
