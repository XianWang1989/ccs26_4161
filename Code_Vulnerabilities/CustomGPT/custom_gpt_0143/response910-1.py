
import subprocess

# Define your Ghostscript command and arguments
ghostscript_path = r'C:\Path\To\gswin32c.exe'
args = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + r'"C:\Path\To\Output.tif"',
    r'"C:\Path\To\Input.pdf"'
]

# Execute the command
try:
    subprocess.check_call(args)
except subprocess.CalledProcessError as e:
    print("An error occurred: ", e)
