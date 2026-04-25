
import subprocess

# Define the paths and arguments
ghostscript_path = 'path/to/gswin32c'
tif_dest = 'path/to/destination/output.tiff'
pdf_source = 'path/to/source/input.pdf'

# Create the command as a list
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
subprocess.Popen(cmd)
