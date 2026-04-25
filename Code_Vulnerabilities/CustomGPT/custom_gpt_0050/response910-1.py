
import subprocess

# Define the paths for Ghostscript and your files
ghostscript_path = "C:\\path\\to\\gswin32c"
tif_dest = "C:\\path\\to\\output.tif"
pdf_source = "C:\\path\\to\\input.pdf"

# Build the command as a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile=" + tif_dest,
    pdf_source
]

# Execute the command
subprocess.Popen(cmd)
