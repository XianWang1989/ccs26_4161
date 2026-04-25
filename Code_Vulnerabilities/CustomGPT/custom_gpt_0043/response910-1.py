
import os

# Paths to Ghostscript executable, input PDF, and output TIFF
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'
pdf_source = r'C:\Path With Spaces\input.pdf'
tif_dest = r'C:\Path With Spaces\output.tif'

# Create the command ensuring paths with spaces are quoted
cmd = '"{}" -q -dNOPAUSE -dBATCH -sDEVICE=tiffg4 -r196X204 -sPAPERSIZE=a4 -sOutputFile="{}" "{}"'.format(
    ghostscript_path, tif_dest, pdf_source
)

# Execute the command
os.popen(cmd)
