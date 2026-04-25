
import subprocess

# Define Ghostscript command and arguments
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

# Execute the command
try:
    result = subprocess.Popen([ghostscript_path] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()

    if result.returncode == 0:
        print("Ghostscript executed successfully.")
        print(stdout.decode())  # Use .decode() to convert bytes to string if needed
    else:
        print("Error executing Ghostscript:")
        print(stderr.decode())

except Exception as e:
    print("An error occurred:", e)
