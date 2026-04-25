
import subprocess

# Define your paths and arguments
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c.exe"
pdf_source = "C:\\path\\to\\input file.pdf"
tif_dest = "C:\\path\\to\\output file.tiff"

# Create the command and arguments as a list
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
subprocess.call(cmd)
