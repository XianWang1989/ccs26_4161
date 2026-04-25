
import subprocess

# Define the paths
ghostscript_path = 'C:\\path\\to\\gswin32c.exe'
tif_dest = 'C:\\path\\to\\output.tif'
pdf_source = 'C:\\path\\to\\source.pdf'

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
