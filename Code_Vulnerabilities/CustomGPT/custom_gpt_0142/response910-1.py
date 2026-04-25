
import subprocess

# Specify the paths and options
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c.exe"
pdf_source = "C:\\path with spaces\\input.pdf"
tif_dest = "C:\\path with spaces\\output.tiff"

# Create the command as a list
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),  # Use format for better clarity
    pdf_source
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print("Error:", stderr)
else:
    print("Output:", stdout)
