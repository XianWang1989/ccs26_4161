
import subprocess

# Paths and command arguments
ghostscript_path = r'C:\path\to\ghostscript\gswin32c'
tif_dest = r'C:\path\to\output.tif'
pdf_source = r'C:\path\to\input.pdf'

# Construct the command with individual arguments
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

# Check for errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Success:", stdout)
