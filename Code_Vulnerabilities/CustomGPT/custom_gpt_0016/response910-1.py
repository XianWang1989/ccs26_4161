
import subprocess

# Define the paths and command
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c"
tif_dest = "C:\\path\\to\\output\\file.tiff"
pdf_source = "C:\\path\\to\\input\\file.pdf"

# Construct the command as a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196x204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),
    pdf_source
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and errors, if any
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Output:", stdout)
