
import subprocess

# Paths to Ghostscript executable and files
ghostscript_path = r'C:\Path\To\gswin32c.exe'
tif_dest = r'C:\Path\To\Output.tif'
pdf_source = r'C:\Path\To\Source.pdf'

# Build the command with a list of arguments
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
