
import subprocess as sp

# Change to the input directory
sp.call(['cd', input_dir], shell=True)

# Loop through the account numbers and execute the ls command
proc_out_list = []
for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc_out.communicate()
    proc_out_list.append((output.decode(), error.decode()))

# Print the outputs
for output, error in proc_out_list:
    print('Output:', output)
    print('Error:', error)
