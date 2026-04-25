
import subprocess

# Define paths (with spaces if needed)
ghostscript_path = r'C:\Path\To\ghostscript\gswin32c.exe'
tif_dest = r'C:\Output\path\output.tiff'
pdf_source = r'C:\Input\path\input.pdf'

# Build argument list
args = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(args)
