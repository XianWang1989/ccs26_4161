
import subprocess

# Define the Ghostscript command and arguments
ghostscript_path = r'C:\Path\To\Ghostscript\bin\gswin32c.exe'
tif_dest = r'C:\Path\To\Output\output.tif'
pdf_source = r'C:\Path\To\Input\input.pdf'

# Create the command as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Optionally handle output
if process.returncode == 0:
    print("Success:", stdout)
else:
    print("Error:", stderr)
