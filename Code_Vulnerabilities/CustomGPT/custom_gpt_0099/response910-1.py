
import subprocess

# Define the paths and command
ghostscript_path = r'C:\Path\To\ghostscript\gswin32c.exe'  # Update with the actual path
pdf_source = r'C:\Path\To\Your PDF.pdf'  # Update with actual path
tif_dest = r'C:\Path\To\Output.tif'  # Update with actual path

# Construct the command as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,  # Using '=' to avoid quotes around the filename
    pdf_source
]

# Execute the command
subprocess.call(cmd)
