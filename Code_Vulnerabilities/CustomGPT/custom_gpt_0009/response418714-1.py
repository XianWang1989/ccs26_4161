
import subprocess as sp

input_dir = 'your_input_directory'  # specify your input directory here
piv_id_list = ['1000', '1001']  # example account numbers
proc_out_list = []

# Change the working directory using Popen
sp.Popen(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Use shell=True to enable wildcard expansion
    proc_out = sp.Popen(f'ls -lh *CSV*APP*{e}.zip', shell=True, cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # Capture output and errors
    proc_out_list.append(out)

    if err:
        print(f"Error: {err.decode().strip()}")
    else:
        print(out.decode().strip())
