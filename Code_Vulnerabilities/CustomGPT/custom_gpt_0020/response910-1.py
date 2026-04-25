
import os

# Define path to Ghostscript executable
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\gswin32c.exe'

# Define arguments
options = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile="{}"'.format(tifDest),  # Wrap output file path in quotes
    '"{}"'.format(pdfSource)               # Wrap input file path in quotes
]

# Join the command with spaces
cmd = '{} {}'.format(ghostscript_path, ' '.join(options))

# Execute command
os.popen(cmd)
