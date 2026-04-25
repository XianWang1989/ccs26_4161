
import subprocess as sp

input_dir = '/path/to/your/directory'  # Replace with your actual directory
piv_id_list = ['1000', '1001']  # Example account numbers
proc_out_list = []

for e in piv_id_list:
    # Use shell=True to allow wildcard expansion
    command = f"cd {input_dir} && ls -lh *CSV*APP*{e}.zip"
    proc_out = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    # Collect the output and error
    out, err = proc_out.communicate()
    proc_out_list.append((out.decode('utf-8'), err.decode('utf-8')))

    # Print the output and any errors
    if out:
        print(out.decode('utf-8'))
    if err:
        print(f"Error: {err.decode('utf-8')}")

# Example output processing (optional)
for output, error in proc_out_list:
    if output:
        print(f"Command output: {output.strip()}")
    if error:
        print(f"Command error: {error.strip()}")
