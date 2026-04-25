
import subprocess

# Paths to the Ghostscript executable and your files
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'
tif_dest = r'C:\Path\To\Output\output_file.tiff'
pdf_source = r'C:\Path\To\Input\input_file.pdf'

# Constructing the command with proper argument handling
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

# Running the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("An error occurred: {}".format(e))
