
import subprocess as sp

# Set the input directory
input_dir = '/path/to/your/directory'  # Update this path
piv_id_list = ['1000', '1001']  # Example account numbers

# Loop through account numbers and run the ls command
for e in piv_id_list:
    command = f'ls -lh {input_dir}/*CSV*APP*{e}.zip'
    proc_out = sp.run(command, shell=True, capture_output=True, text=True)

    if proc_out.returncode == 0:
        print(proc_out.stdout)  # Successful output
    else:
        print(f"Error: {proc_out.stderr}")  # Error output
