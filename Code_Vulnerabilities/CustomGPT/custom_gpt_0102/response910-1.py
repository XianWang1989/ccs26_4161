
import subprocess

# Define your paths safely
ghostscript_path = 'C:\\Path\\To\\gswin32c.exe'
tifDest = 'C:\\Path\\To\\output.tiff'
pdfSource = 'C:\\Path\\To\\input.pdf'

# Create the command as a list
cmd = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tifDest),
    pdfSource
]

# Execute the command
subprocess.call(cmd)
