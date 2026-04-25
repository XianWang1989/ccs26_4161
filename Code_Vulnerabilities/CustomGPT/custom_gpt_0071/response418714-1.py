
import subprocess as sp

input_dir = '/path/to/your/directory'  # Change this to your directory
piv_id_list = ['1000', '1001']  # Sample account numbers
proc_out_list = []

for e in piv_id_list:
    # Run the ls command in the specified directory
    proc_out = sp.Popen(
        ['ls', '-lh', f'*CSV*APP*{e}.zip'],
        cwd=input_dir,
        stdout=sp.PIPE,
        stderr=sp.PIPE
    )

    # Capture output and errors
    stdout, stderr = proc_out.communicate()

    # Print the result
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
