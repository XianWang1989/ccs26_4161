
import subprocess

ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c'
tif_dest = r'C:\Path\To\Output\output.tiff'
pdf_source = r'C:\Path\To\Source\source.pdf'

# Create the command as a list of arguments
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
    subprocess.call(cmd)
except Exception as e:
    print("An error occurred: {}".format(e))
