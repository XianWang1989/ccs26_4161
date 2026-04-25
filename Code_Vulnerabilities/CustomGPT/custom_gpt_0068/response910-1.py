
import subprocess

# Define the paths and arguments
ghostscript_path = r'C:\Path\To\Ghostscript\gswin32c.exe'  # Adjust the path to gswin32c
tif_dest = r'C:\Path\To\Output\output.tiff'  # Adjust this to your output TIFF file path
pdf_source = r'C:\Path\To\Input\input.pdf'  # Adjust this to your input PDF file path

# Prepare the command and arguments list
command = [
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
subprocess.call(command)
