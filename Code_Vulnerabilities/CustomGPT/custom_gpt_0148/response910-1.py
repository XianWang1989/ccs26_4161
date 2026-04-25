
import subprocess

# Define your Ghostscript command and arguments
gs_path = self._ghostscriptPath + 'gswin32c'
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

# Execute the command
try:
    subprocess.call([gs_path] + args)
except Exception as e:
    print(f"Error: {e}")
