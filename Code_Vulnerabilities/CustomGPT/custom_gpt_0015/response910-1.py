
import subprocess

# Paths and arguments
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
pdf_source = r"C:\Path With Spaces\file.pdf"
tif_dest = r"C:\Path With Spaces\output.tiff"

# Construct the command as a list
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
