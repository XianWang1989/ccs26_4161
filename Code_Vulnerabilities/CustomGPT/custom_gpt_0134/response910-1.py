
import subprocess

# Define the command and its arguments
ghostscript_path = 'C:\\path\\to\\ghostscript\\gswin32c.exe'
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + '"%s"' % tifDest,
    pdfSource
]

# Construct the full command
cmd = [ghostscript_path] + args

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture output and errors
stdout, stderr = process.communicate()

# Check if the execution was successful
if process.returncode == 0:
    print("Execution successful:", stdout)
else:
    print("Error:", stderr)
