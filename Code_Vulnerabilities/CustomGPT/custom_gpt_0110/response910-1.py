
import subprocess

# Path to Ghostscript executable
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'

# Define arguments as a list
args = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + '"%s"' % tifDest,
    pdfSource
]

# Execute the command
subprocess.call(args)
