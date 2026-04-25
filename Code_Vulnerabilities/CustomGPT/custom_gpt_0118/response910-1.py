
import subprocess

# Paths and filenames
ghostscript_path = r"C:\path\to\gswin32c"
pdf_source = r"C:\path\to\source.pdf"
tif_dest = r"C:\path\to\output.tiff"

# Command as a list of arguments
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
