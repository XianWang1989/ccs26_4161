
import subprocess

# Paths to Ghostscript and your files
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c"
tif_dest = "C:\\path\\to\\output\\file.tif"
pdf_source = "C:\\path\\to\\input\\file.pdf"

# Command and arguments
args = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),  # Use format to insert output path
    pdf_source
]

# Execute the command
process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Optional: print output and error if any
if stdout:
    print("Output:", stdout.decode())
if stderr:
    print("Error:", stderr.decode())
