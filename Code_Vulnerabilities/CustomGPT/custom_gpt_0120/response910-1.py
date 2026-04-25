
import subprocess

# Define your paths and arguments
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\gswin32c.exe'
pdf_source = 'C:\\Path With Spaces\\source.pdf'
tif_dest = 'C:\\Path With Spaces\\output.tiff'

# Prepare the command and arguments
command = [
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
subprocess.call(command)
