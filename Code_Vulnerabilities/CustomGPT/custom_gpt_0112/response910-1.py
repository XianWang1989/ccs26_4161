
import subprocess
import shlex

# Define your paths and command
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'
tifDest = r'C:\Output\output.tif'
pdfSource = r'C:\Input\input.pdf'

# Create the command arguments list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tifDest,
    pdfSource
]

# Execute the command
subprocess.call(cmd)
