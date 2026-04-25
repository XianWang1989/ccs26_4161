
import subprocess

# Paths to your files (with spaces handled)
tif_dest = r'path\to\output.tif'
pdf_source = r'path\to\input.pdf'
ghostscript_path = r'path\to\gswin32c.exe'

# Command arguments
args = [
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
subprocess.call(args)
