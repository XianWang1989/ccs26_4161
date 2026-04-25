
import subprocess

# Paths to Ghostscript and your files
ghostscript_path = 'C:\\Path\\To\\gswin32c.exe'
tif_dest = 'C:\\Path\\To\\output.tiff'
pdf_source = 'C:\\Path\\To\\input.pdf'

# Construct the command as a list of arguments
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
subprocess.Popen(cmd)
