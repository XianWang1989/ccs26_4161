
import subprocess

# Define the paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tifDest,
    pdfSource
]

# Construct the command
cmd = [ghostscript_path] + args

# Execute the command
try:
    # Use subprocess.run if you're using Python 3.5+, for Python 2.3 use subprocess.call
    subprocess.call(cmd)
except Exception as e:
    print("An error occurred:", e)
