
import subprocess

# Define paths and arguments
ghostscript_path = r"C:\Path\To\gswin32c"
tif_dest = r"C:\Path\To\output.tiff"
pdf_source = r"C:\Path\To\input.pdf"

# Build the command as a list of arguments
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
subprocess.call(cmd)
