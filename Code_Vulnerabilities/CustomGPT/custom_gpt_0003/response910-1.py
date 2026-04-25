
import subprocess

# Example paths and parameters
ghostscript_path = "C:\\path\\to\\ghostscript\\gswin32c.exe"
pdf_source = "C:\\path\\to\\file with spaces\\source.pdf"
tif_dest = "C:\\path\\to\\output with spaces\\output.tiff"

# Build command as a list
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
    subprocess.run(cmd, check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
