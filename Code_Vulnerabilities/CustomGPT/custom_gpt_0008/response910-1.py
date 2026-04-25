
import subprocess

# Define the paths and arguments
ghostscript_path = r"C:\Path\To\gswin32c.exe"
tif_dest = r"C:\Path\To\output.tiff"
pdf_source = r"C:\Path\To\input.pdf"

# Create the command as a list
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
subprocess.Popen(cmd, shell=True)
