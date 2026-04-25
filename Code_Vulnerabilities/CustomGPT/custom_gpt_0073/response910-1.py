
import subprocess

# Paths and arguments
ghostscript_path = 'C:\\path\\to\\gswin32c'
tif_dest = '"C:\\path\\to\\output.tif"'  # Ensure paths are quoted
pdf_source = '"C:\\path\\to\\input.pdf"'

# Command list
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
subprocess.Popen(cmd)
