
import subprocess

# Path to Ghostscript executable
ghostscript_path = 'C:\\Path\\To\\gswin32c.exe'
# Arguments
args = [
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile="{}"'.format(tif_dest),
    pdf_source
]

# Combine everything into one command list
command = [ghostscript_path] + args

try:
    # Execute the command
    subprocess.check_call(command)
except subprocess.CalledProcessError as e:
    print("An error occurred: {}".format(e))
