
import subprocess

# Define paths (ensure these paths are correct)
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
tif_dest = r"C:\Path\To\Output\file.tif"
pdf_source = r"C:\Path\To\Input\file.pdf"

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
    subprocess.run(cmd, check=True)
    print("Ghostscript executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error occurred while executing Ghostscript: {}".format(e))
