
import subprocess

# Define the paths for Ghostscript, PDF source, and TIFF destination
ghostscript_path = "C:\\path\\to\\gswin32c.exe"
pdf_source = "C:\\path\\to\\source.pdf"
tif_dest = "C:\\path\\to\\output.tif"

# Create a command list to pass arguments safely
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
