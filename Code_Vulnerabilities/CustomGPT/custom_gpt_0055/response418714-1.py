
import subprocess as sp

input_dir = '/path/to/your/directory'  # Set your input directory
piv_id_list = ['1000', '2000']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # Construct the file pattern
    file_pattern = '*CSV*APP*{0}.zip'.format(e)
    # Run the ls command in the specified directory
    proc_out = sp.Popen(['ls', '-lh', file_pattern], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture the output and error
    if proc_out.returncode == 0:
        print(out.decode())  # Print the output if successful
    else:
        print(f"Error: {err.decode()}")  # Print the error if there's a problem
