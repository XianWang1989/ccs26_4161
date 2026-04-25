
import subprocess

# Define the paths
ghostscript_path = r'C:\Path\To\gswin32c.exe'
pdf_source = r'C:\Path\To\your pdf file.pdf'
tif_dest = r'C:\Path\To\your output.tiff'

# Create the command as a list to handle spaces properly
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
subprocess.Popen(cmd, shell=True)
