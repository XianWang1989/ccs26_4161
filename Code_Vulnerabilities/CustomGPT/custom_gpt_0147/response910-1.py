
import subprocess

# Define the paths and arguments
ghostscript_path = self._ghostscriptPath + 'gswin32c'  # Path to Ghostscript executable
arguments = [
    '-q', 
    '-dNOPAUSE', 
    '-dBATCH',
    '-sDEVICE=tiffg4', 
    '-r196X204',
    '-sPAPERSIZE=a4', 
    '-sOutputFile={}'.format(tifDest),  # Properly formatted destination
    pdfSource  # Source PDF file
]

# Combine the executable and the arguments
cmd = [ghostscript_path] + arguments

# Execute the command using subprocess.Popen
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check the result of the execution
if process.returncode != 0:
    print("Error executing Ghostscript:", stderr)
else:
    print("Ghostscript executed successfully:", stdout)
