
import subprocess as sp

# Assuming input_dir and piv_id_list are already defined
proc_out_list = []
for e in piv_id_list:
    # Construct the command as a single string
    command = "ls -lh *CSV*APP*{0}.zip".format(e)
    # Run the command through a shell
    proc_out = sp.run(command, shell=True, cwd=input_dir, capture_output=True, text=True)
    proc_out_list.append(proc_out)
    print(proc_out.stdout)  # Print the output of the command
