
import subprocess

ghostscript_path = "C:\\path\\to\\gswin32c"
tif_dest = "C:\\path\\to\\output.tiff"
pdf_source = "C:\\path\\to\\input.pdf"

# Construct the command and arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196x204",
    "-sPAPERSIZE=a4",
    "-sOutputFile=" + tif_dest,
    pdf_source
]

# Execute the command
subprocess.Popen(cmd)
