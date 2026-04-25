
import subprocess

# Define your paths and arguments
ghostscript_path = 'C:\\Path\\To\\gswin32c'
tif_dest = 'C:\\Path\\To\\output.tiff'
pdf_source = 'C:\\Path\\To\\source.pdf'

# Create the command as a list to handle spaces and arguments properly
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
