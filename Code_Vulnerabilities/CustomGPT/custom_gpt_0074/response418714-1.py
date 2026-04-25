
import subprocess as sp

input_dir = '/path/to/your/directory'  # Specify your input directory here
piv_id_list = ['1000', '1001']  # Sample list of IDs
proc_out_list = []  # Initialize list to collect processes

for i, e in enumerate(piv_id_list):
    # Construct the pattern to search for the file
    file_pattern = '*CSV*APP*{0}.zip'.format(e)

    # Call ls with the correct directory and file pattern
    proc_out = sp.Popen(['ls', '-lh', file_pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)

    # Capture output and error
    output, error = proc_out.communicate()

    if output:
        print(output.decode())  # Print file details if any
    if error:
        print(error.decode())  # Print error message if any

    proc_out_list.append(proc_out)
