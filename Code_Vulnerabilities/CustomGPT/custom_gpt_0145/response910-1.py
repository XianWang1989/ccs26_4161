
import subprocess

# Define your command and arguments
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
tif_dest = r"C:\Path With Spaces\output.tif"
pdf_source = r"C:\Another Path With Spaces\input.pdf"

# Construct the command with arguments
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
except subprocess.CalledProcessError as e:
    print("An error occurred while executing Ghostscript: {}".format(e))
