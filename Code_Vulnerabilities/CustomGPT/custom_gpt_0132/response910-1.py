
import subprocess

# Define your paths
ghostscript_path = self._ghostscriptPath + 'gswin32c'
tif_dest = 'output.tiff'
pdf_source = 'input.pdf'

# Prepare the command and its arguments
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
subprocess.Popen(cmd, shell=True)
