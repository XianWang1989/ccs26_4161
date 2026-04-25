
import subprocess

# Define paths and arguments
ghostscript_path = 'C:\\Path\\To\\ghostscript\\gswin32c'
tif_dest = 'C:\\Path With Spaces\\output.tif'
pdf_source = 'C:\\Path With Spaces\\input.pdf'

# Create the command as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(cmd)
