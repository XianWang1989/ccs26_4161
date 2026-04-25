
import subprocess

# Define your paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tifDest),  # Use format for safe substitution
    pdfSource
]

# Execute the command
subprocess.call([ghostscript_path] + args)
