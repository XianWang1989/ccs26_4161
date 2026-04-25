
import subprocess

# Paths to Ghostscript, the PDF source, and the TIFF destination
ghostscript_path = r'C:\path\to\gswin32c.exe'
tif_dest = r'C:\path\to\output.tif'
pdf_source = r'C:\path\to\input.pdf'

# Command and arguments as a list
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
