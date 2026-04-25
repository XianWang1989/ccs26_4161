
import subprocess

# Define the paths and options
ghostscript_path = self._ghostscriptPath + 'gswin32c'
options = [
    '-q', 
    '-dNOPAUSE', 
    '-dBATCH', 
    '-sDEVICE=tiffg4', 
    '-r196x204', 
    '-sPAPERSIZE=a4', 
    '-sOutputFile=' + '"' + tifDest + '"', 
    '"' + pdfSource + '"'
]

# Construct the command
cmd = [ghostscript_path] + options

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Output:", stdout)
