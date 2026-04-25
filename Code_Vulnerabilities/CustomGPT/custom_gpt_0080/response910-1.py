
import subprocess

# Define your command and arguments
ghostscript_path = "C:\\Path\\To\\ghostscript\\gswin32c.exe"
tif_dest = "C:\\Path\\To\\Output\\output.tiff"
pdf_source = "C:\\Path\\To\\Input\\input.pdf"

# Create a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),
    pdf_source
]

# Execute the command
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    print("Error executing Ghostscript:", e)
