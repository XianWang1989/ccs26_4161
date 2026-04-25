
import subprocess

# Define the Ghostscript executable path and the command arguments
ghostscript_path = r"C:\Path\To\gswin32c.exe"  # Adjust the path as per your installation
tif_dest = r"C:\Path\To\output.tiff"  # Path for the output TIFF file
pdf_source = r"C:\Path\To\input.pdf"  # Path for the input PDF file

# Build the command as a list of arguments
cmd = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196x204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tif_dest),  # Format the output file path
    pdf_source  # The input PDF file path
]

# Execute the command
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()  # Wait for the process to complete and capture output

# Check for errors
if process.returncode != 0:
    print("Error occurred:", stderr)
else:
    print("Ghostscript executed successfully:", stdout)
