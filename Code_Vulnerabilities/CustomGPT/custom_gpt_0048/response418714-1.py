
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set to your directory
piv_id_list = ['1000', '1001', '1002']  # Example list of IDs
proc_out_list = []

# Change directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Prepare the command string
    cmd = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    # Run the command with shell=True
    proc_out = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    # Print output or error message
    if out:
        print(out.decode())
    if err:
        print(err.decode())
