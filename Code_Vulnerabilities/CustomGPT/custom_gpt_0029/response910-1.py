
import subprocess

# Define the paths and arguments
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

# Combine the command and arguments
cmd = [ghostscript_path] + arguments

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Optionally handle output or errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Success:", stdout)
