
import subprocess

# Define your paths
ghostscript_path = 'C:\\path\\to\\gswin32c'
pdf_source = 'C:\\path\\to\\your document.pdf'  # Path with spaces
tif_dest = 'C:\\path\\to\\output.tiff'

# Construct the command as a list
cmd = [
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
subprocess.Popen(cmd, shell=True).wait()
