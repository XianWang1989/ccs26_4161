
import subprocess

# Define the paths and command
ghostscript_path = r"C:\path\to\ghostscript\gswin32c.exe"
tif_dest = r"C:\path\to\output\output.tif"
pdf_source = r"C:\path\to\input\input.pdf"

# Create the command with arguments in a list
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
