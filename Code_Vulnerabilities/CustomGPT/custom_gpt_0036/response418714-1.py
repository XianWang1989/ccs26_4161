
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Change the current directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, errors = proc_out.communicate()  # Get the output and errors
    proc_out_list.append(output)

    if output:
        print(output.decode())  # decode the byte output to string
    if errors:
        print(errors.decode(), file=sys.stderr)  # print errors if any
