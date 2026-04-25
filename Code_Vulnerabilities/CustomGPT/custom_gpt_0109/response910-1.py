
import subprocess

# Define the Ghostscript command and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tifDest,  # Ensure this variable contains the full path
    pdfSource                   # Ensure this variable contains the full path
]

# Execute the command
try:
    subprocess.call([ghostscript_path] + args)
except Exception as e:
    print("An error occurred: {}".format(e))
