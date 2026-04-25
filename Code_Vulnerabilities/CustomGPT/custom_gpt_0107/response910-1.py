
import subprocess

# Define paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
arguments = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tifDest),  # Use .format for better readability
    pdfSource
]

# Combine all parts into a single command
cmd = [ghostscript_path] + arguments

# Execute command
subprocess.call(cmd)
