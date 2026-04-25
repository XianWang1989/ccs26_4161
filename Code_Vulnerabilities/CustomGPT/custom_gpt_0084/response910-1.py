
import subprocess

# Define variables for paths
ghostscript_path = r'C:\Path\To\gswin32c'
tif_dest = r'C:\Path\To\output.tif'
pdf_source = r'C:\Path\To\input.pdf'

# Prepare the command and arguments
cmd = [ghostscript_path, '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=tiffg4',
       '-r196x204', '-sPAPERSIZE=a4', '-sOutputFile=' + tif_dest, pdf_source]

# Execute the command
try:
    subprocess.call(cmd)
except OSError as e:
    print("Execution failed: ", e)
