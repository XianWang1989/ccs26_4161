
import subprocess

# Define paths and arguments
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c'
tif_dest = r'C:\Path\To\Output\output.tif'
pdf_source = r'C:\Path\To\Input\input.pdf'

# Prepare the command and arguments
cmd = [
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
subprocess.call(cmd)
