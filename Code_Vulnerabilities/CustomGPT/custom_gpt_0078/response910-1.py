
import os
import subprocess

# Paths to Ghostscript and files
ghostscript_path = r"C:\Path\To\ghostscript\gswin32c.exe"
tif_dest = r"C:\Path\To\output.tiff"
pdf_source = r"C:\Path\To\input.pdf"

# Build the command with arguments
command = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
subprocess.call(command)
