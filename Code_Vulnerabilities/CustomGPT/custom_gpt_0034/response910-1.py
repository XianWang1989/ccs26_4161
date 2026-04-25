
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
    '-sOutputFile={}'.format(tifDest),
    pdfSource
]

# Use subprocess to execute the command
process = subprocess.Popen([ghostscript_path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Success:", stdout)
