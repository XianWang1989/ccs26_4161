
import subprocess

# Paths and arguments
ghostscript_path = r'C:\path\to\gswin32c'
tif_dest = r'C:\path\to\output.tif'
pdf_source = r'C:\path\to\input.pdf'

# Construct the command as a list
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
