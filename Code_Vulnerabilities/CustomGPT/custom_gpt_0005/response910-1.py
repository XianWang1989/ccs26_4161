
import subprocess

# Define the paths and command
ghostscript_path = r"C:\Path\To\gswin32c"
tif_dest = r"C:\Path\To\output.tif"
pdf_source = r"C:\Path\To\input.pdf"

# Prepare the command as a list
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile=" + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(cmd)
