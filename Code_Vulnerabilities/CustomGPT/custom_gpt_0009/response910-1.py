
import subprocess

# Define paths
ghostscript_path = self._ghostscriptPath + 'gswin32c'
tif_dest = 'C:\\path to output\\output.tif'
pdf_source = 'C:\\path to input\\input.pdf'

# Build the command as a list, quoting arguments that may contain spaces
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(cmd)
