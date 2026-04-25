
import subprocess

# Paths to Ghostscript and files
ghostscript_path = "C:\\Path\\To\\gswin32c.exe"
tif_dest = "C:\\Path With Spaces\\output.tif"
pdf_source = "C:\\Another Path With Spaces\\input.pdf"

# Construct the command as a list of arguments
command = [
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
subprocess.call(command)
