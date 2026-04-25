
import subprocess

# Define your paths and parameters
ghostscript_path = 'C:\\path\\to\\gswin32c'
pdf_source = 'C:\\path\\to\\your file.pdf'
tif_dest = 'C:\\path\\to\\output.tif'

# Construct the command and arguments as a list
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

# Get output and errors, if any
stdout, stderr = process.communicate()

# Print output for debugging
print(stdout)
if stderr:
    print("Error:", stderr)
