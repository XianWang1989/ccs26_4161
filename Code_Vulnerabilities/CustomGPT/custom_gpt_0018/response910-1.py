
import subprocess

# Define your paths and arguments
ghostscript_path = r"C:\path\to\ghostscript\gswin32c.exe"
tif_dest = r"C:\output\path\output.tiff"
pdf_source = r"C:\input\path\source.pdf"

# Create the command as a list of arguments
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
subprocess.call(cmd)
