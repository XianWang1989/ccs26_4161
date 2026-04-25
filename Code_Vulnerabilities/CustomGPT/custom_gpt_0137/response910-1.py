
import subprocess

# Define the path to Ghostscript executable and the arguments
ghostscript_path = "C:\\Path\\To\\Ghostscript\\gswin32c.exe"
pdf_source = "C:\\Path With Spaces\\input.pdf"
tif_dest = "C:\\Path With Spaces\\output.tiff"

# Create the command list
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),
    pdf_source,
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture output and errors
stdout, stderr = process.communicate()

# Print the results
if process.returncode == 0:
    print("Success:", stdout)
else:
    print("Error:", stderr)
