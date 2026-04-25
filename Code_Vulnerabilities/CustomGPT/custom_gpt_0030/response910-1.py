
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
    '-sOutputFile={}'.format(tifDest),  # Use .format for clarity
    pdfSource
]

# Execute the command
try:
    process = subprocess.Popen([ghostscript_path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        print("Success:", output)
    else:
        print("Error:", error)
except Exception as e:
    print("An error occurred:", str(e))
