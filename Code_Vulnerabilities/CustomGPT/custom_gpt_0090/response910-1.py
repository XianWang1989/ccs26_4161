
import subprocess

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

# Combine the executable and arguments
command = [ghostscript_path] + args

# Execute the command
subprocess.Popen(command)
