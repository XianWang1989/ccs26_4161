
import subprocess

# Define paths and command arguments
ghostscript_path = r'C:\path\to\gswin32c.exe'
tif_dest = r'C:\path\to\output.tif'
pdf_source = r'C:\path\to\input.pdf'

# Build the command as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("An error occurred: {}".format(e))
