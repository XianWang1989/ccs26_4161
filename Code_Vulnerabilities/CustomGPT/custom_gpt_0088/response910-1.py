
import subprocess

# Define the paths and arguments
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\gswin32c'
tif_dest = 'C:\\Path With Spaces\\output.tif'
pdf_source = 'C:\\Path With Spaces\\input.pdf'

# Create a list of arguments
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
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
