
import os
import subprocess as sp

# Change to the input directory
input_dir = 'your_directory_here'  # Replace with your actual directory
os.chdir(input_dir)

proc_out_list = []

# Loop through your account numbers
for e in piv_id_list:
    command = 'ls -lh *CSV*APP*{0}.zip'.format(e)

    # Use shell=True to enable wildcard expansion
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    # Append the output if needed
    proc_out_list.append(proc_out.stdout.strip())

    # Print the standard output
    print(proc_out.stdout)

    # Print the error if there is one
    if proc_out.stderr:
        print("Error:", proc_out.stderr)
