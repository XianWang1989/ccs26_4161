
import subprocess

# Define the paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
pdf_source = 'C:\\path\\to\\your\\file.pdf'
tif_dest = 'C:\\path\\to\\your\\output.tif'

# Create the command as a list
cmd = [
    ghostscript_path, '-q', '-dNOPAUSE', '-dBATCH',
    '-sDEVICE=tiffg4', '-r196x204', '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("An error occurred while executing Ghostscript: {}".format(e))
