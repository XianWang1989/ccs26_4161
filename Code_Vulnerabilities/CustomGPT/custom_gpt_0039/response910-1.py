
import subprocess

# Define the paths and arguments
ghostscript_path = 'C:\\Path\\To\\gswin32c.exe'
tif_dest = 'C:\\Path With Spaces\\output.tif'
pdf_source = 'C:\\Another Path With Spaces\\input.pdf'

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
