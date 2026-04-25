
import subprocess

# Paths and arguments
ghostscript_path = r'C:\path\to\ghostscript\gswin32c.exe'
tif_dest = r'C:\path\to\output\file.tif'
pdf_source = r'C:\path\to\input\file.pdf'

# Prepare the command with a list
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
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check if there were any errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Output:", stdout)
