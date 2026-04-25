
import subprocess as sp
import os

# Change to the desired directory
os.chdir(input_dir)

proc_out_list = []
for e in piv_id_list:
    filename = f'*CSV*APP*{e}.zip'
    try:
        # Use glob to match the file pattern
        files = glob.glob(filename)
        if files:
            for f in files:
                # Call ls for each found file
                proc_out = sp.Popen(['ls', '-lh', f], stdout=sp.PIPE, stderr=sp.PIPE)
                out, err = proc_out.communicate()
                print(out.decode())
        else:
            print(f"No files found for {filename}")
    except Exception as ex:
        print(f"Error: {ex}")
