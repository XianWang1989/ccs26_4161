
import subprocess as sp

# Change to the input directory
input_dir = '/path/to/your/directory'  # Specify the correct path
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

# Use shell=True to allow wildcard expansion
for i, e in enumerate(piv_id_list):
    command = f'ls -lh *CSV*APP*{e}.zip'
    proc_out = sp.Popen(command, shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()

    # Store the output and possible errors
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))
    print(f'Output for {e}: {out.decode("utf-8")}')
    if err:
        print(f'Error for {e}: {err.decode("utf-8")}')
