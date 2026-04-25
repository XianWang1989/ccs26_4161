
import subprocess

# Define your Ghostscript command and arguments
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c'  # Update with your Ghostscript path
tif_dest = r'C:\Path\To\Output\output.tiff'  # Output file path
pdf_source = r'C:\Path\To\Input\input.pdf'  # Input PDF file path

# Create a list of command arguments
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Print the output and errors if any
if process.returncode == 0:
    print("Ghostscript executed successfully.")
else:
    print("Error executing Ghostscript:", stderr.decode())
