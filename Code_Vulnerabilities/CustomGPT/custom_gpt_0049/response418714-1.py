
import subprocess as sp

input_dir = '/path/to/your/directory'  # Specify your input directory here
piv_id_list = ['1000', '1001', '1002']  # Sample account number list
proc_out_list = []

for e in piv_id_list:
    proc_out = sp.Popen(['ls', '-lh', '*CSV*APP*{0}.zip'.format(e)], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Wait for the command to complete and fetch output/errors
    proc_out_list.append(out.decode().strip())  # Decode the output
    if err:
        print(err.decode().strip())  # Print any errors if they occur

for result in proc_out_list:
    print(result)  # Print the results
