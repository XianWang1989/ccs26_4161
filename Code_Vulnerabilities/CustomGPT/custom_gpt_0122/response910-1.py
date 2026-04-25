
import subprocess

# Define paths and arguments
ghostscript_path = r'C:\path\to\ghostscript\gswin32c.exe'
tif_dest = r'C:\path\to\output.tiff'
pdf_source = r'C:\path\to\input.pdf'

# Construct the command with arguments as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
subprocess.call(cmd)
