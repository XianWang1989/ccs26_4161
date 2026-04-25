
import subprocess

# Define the paths and arguments
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c.exe"
tif_dest = "C:\\path\\to\\output\\output.tiff"
pdf_source = "C:\\path\\to\\input\\input.pdf"

# Create the command as a list of arguments
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
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("Error:", e)
