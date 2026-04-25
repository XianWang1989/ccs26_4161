
import subprocess

# Define paths and command
ghostscript_path = 'C:\\path\\to\\gswin32c.exe'
tif_dest = 'C:\\path\\to\\output\\file.tiff'
pdf_source = 'C:\\path\\to\\input\\file.pdf'

# List command and arguments
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
