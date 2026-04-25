
import subprocess

# Define the paths and the command
ghostscript_path = self._ghostscriptPath + 'gswin32c'
arguments = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tifDest,
    pdfSource
]

# Construct the command and execute it
try:
    subprocess.call([ghostscript_path] + arguments)
except Exception as e:
    print("An error occurred: {}".format(e))
