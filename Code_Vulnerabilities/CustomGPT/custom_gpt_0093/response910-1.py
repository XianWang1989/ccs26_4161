
import subprocess

# Define paths and arguments
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'  # Update with actual path
tif_dest = r'C:\Path\To\Output\output.tiff'  # Destination TIFF path
pdf_source = r'C:\Path\To\Input\input.pdf'     # Source PDF path

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
subprocess.call(cmd)
