
import subprocess

# Define paths and arguments
ghostscript_path = 'C:\\path\\to\\gswin32c.exe'  # Adjust this path
tif_dest = 'C:\\output\\path\\output.tiff'
pdf_source = 'C:\\input\\path\\document.pdf'

# Create the command list
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
subprocess.Popen(cmd)
