
import subprocess

# Paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tifDest),  # Make sure tifDest is properly defined
    pdfSource  # Make sure pdfSource is properly defined
]

# Create the command
cmd = [ghostscript_path] + args

# Execute the command
subprocess.Popen(cmd, shell=True)
