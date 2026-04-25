
import subprocess

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

# Create the command and execute it
try:
    process = subprocess.Popen([ghostscript_path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print("Success:", stdout)
    else:
        print("Error:", stderr)
except Exception as e:
    print("An error occurred:", e)
