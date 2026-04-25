
import subprocess

# Define the paths and parameters
ghostscript_path = r"C:\Path\To\ghostscript\gswin32c"  # Update the path
pdf_source = r"C:\Path\To\Your File.pdf"  # Update the path
tif_dest = r"C:\Path\To\Output File.tiff"  # Update the path

# Prepare the command and arguments in a list
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
subprocess.Popen(cmd, shell=True)
