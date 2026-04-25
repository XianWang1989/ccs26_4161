
import os
import shlex

# Define paths and arguments
ghostscript_path = r"C:\path\to\ghostscript\gswin32c.exe"
pdf_source = r"C:\path\to\file with spaces\document.pdf"
tif_dest = r"C:\path\to\output\image.tif"

# Prepare the arguments list
args = [
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

# Combine arguments into a single command
command = ' '.join(shlex.quote(arg) for arg in args)

# Execute the command
os.system(command)
