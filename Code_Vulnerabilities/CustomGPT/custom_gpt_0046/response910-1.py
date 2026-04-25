
import subprocess

# Define paths and arguments
ghostscript_path = 'C:\\Path\\To\\gswin32c.exe'
tif_dest = 'C:\\Output\\OutputFile.tiff'
pdf_source = 'C:\\Path With Spaces\\InputFile.pdf'

# Create the command as a list
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

# Execute the command
subprocess.call(cmd)
