
import subprocess
import shlex

# Define your paths
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
tif_dest = r"C:\Path\To\Output\output.tiff"
pdf_source = r"C:\Path\To\Input\input.pdf"

# Create the command as a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),
    pdf_source
]

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("An error occurred: {}".format(e))
