
import subprocess as sp

input_dir = "/path/to/your/input/directory"  # Update to your actual input directory
piv_id_list = ["1000", "1001"]  # Example list of account numbers
proc_out_list = []

for i, e in enumerate(piv_id_list):
    # Use cwd to specify the directory for the ls command
    proc_out = sp.Popen(['ls', '-lh', f'*CSV*APP*{e}.zip'], cwd=input_dir, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc_out.communicate()  # get the output and error messages
    proc_out_list.append((out.decode(), err.decode()))  # decode output and error messages to strings
    print(out.decode())  # Print the output if any
    if err:
        print("Error:", err.decode())  # Print any errors

# Print results
for index, (output, error) in enumerate(proc_out_list):
    print(f"Result for {piv_id_list[index]}:\n{output}\n{error}")
