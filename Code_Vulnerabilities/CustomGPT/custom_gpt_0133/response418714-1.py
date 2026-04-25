
import subprocess as sp

input_dir = "/path/to/your/directory"  # Specify your input directory
piv_id_list = ["1000", "1001", "1002"]  # Example list of account numbers
proc_out_list = []

# Change the current working directory
sp.call(['cd', input_dir], shell=True)

for e in piv_id_list:
    # Create the wildcard pattern
    pattern = f"*CSV*APP*{e}.zip"
    # Run the 'ls' command and capture its output
    try:
        proc_out = sp.check_output(f'ls -lh {pattern}', shell=True, cwd=input_dir)
        proc_out_list.append(proc_out.decode())
        print(proc_out.decode())
    except sp.CalledProcessError as e:
        print(f"Error: {e.output.decode()}")

# Output the results
for result in proc_out_list:
    print(result)
