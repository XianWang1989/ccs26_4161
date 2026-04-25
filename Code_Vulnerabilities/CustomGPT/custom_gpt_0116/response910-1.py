
import subprocess

# Define the paths and arguments
ghostscript_path = r"C:\Path\To\Ghostscript\gswin32c.exe"
tif_dest = r"C:\Output\file.tiff"
pdf_source = r"C:\Input\file.pdf"

# Construct the command
cmd = [ghostscript_path, '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=tiffg4', 
       '-r196x204', '-sPAPERSIZE=a4', '-sOutputFile=' + tif_dest, pdf_source]

# Execute the command
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
