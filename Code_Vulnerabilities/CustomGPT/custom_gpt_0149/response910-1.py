
import subprocess

# Define the paths and arguments
ghostscript_path = 'C:\\path\\to\\ghostscript\\gswin32c.exe'
tif_dest = 'C:\\path\\to\\output.tiff'
pdf_source = 'C:\\path\\to\\input.pdf'

# Create a list of arguments
args = [
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
subprocess.call(args)
