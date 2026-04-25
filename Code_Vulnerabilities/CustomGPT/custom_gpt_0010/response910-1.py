
import subprocess

# Define paths for Ghostscript and your files
ghostscript_path = r'C:\path\to\gswin32c.exe'
tif_dest = r'C:\path\to\output.tiff'
pdf_source = r'C:\path\to\input.pdf'

# Create the command list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(cmd)
