
import subprocess

ghostscript_path = 'C:\\Path\\To\\Ghostscript\\gswin32c.exe'  # Update with your actual path
pdf_source = 'C:\\Path\\To\\Input File.pdf'  # Input PDF with spaces
tif_dest = 'C:\\Path\\To\\Output File.tif'  # Output TIFF with spaces

# Construct the command as a list of arguments
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

# Use subprocess to execute the command
subprocess.Popen(cmd)
