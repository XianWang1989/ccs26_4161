
import subprocess

# Define the paths and arguments
ghostscript_path = 'C:\\path\\to\\gswin32c.exe'  # Adjust the path as necessary
pdf_source = 'C:\\path\\to\\source.pdf'
tif_dest = 'C:\\path\\to\\destination.tif'

# Create the command as a list of arguments
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
