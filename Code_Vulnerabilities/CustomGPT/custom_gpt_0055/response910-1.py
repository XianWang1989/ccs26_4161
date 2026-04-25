
import subprocess

# Paths with spaces should be enclosed in quotes
ghostscript_path = r"C:\path\to\gswin32c.exe"
tif_dest = r"C:\path\to\output.tif"
pdf_source = r"C:\path\to\input.pdf"

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
subprocess.Popen(cmd, shell=True)
