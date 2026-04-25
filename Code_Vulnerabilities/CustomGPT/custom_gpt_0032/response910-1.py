
import subprocess
import shlex

# Define paths and arguments
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
tif_dest = r"C:\Output\output.tif"
pdf_source = r"C:\Input\file.pdf"

# Construct the command with a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196x204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),
    pdf_source
]

# Execute the command
try:
    subprocess.check_call(cmd)
    print("Ghostscript executed successfully.")
except subprocess.CalledProcessError as e:
    print("An error occurred: {}".format(e))
