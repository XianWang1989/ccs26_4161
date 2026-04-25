
import subprocess

# Define your Ghostscript command and arguments
ghostscript_path = "C:\\Path\\To\\gswin32c.exe"  # Adjust the path to your Ghostscript executable
pdf_source = "C:\\Path\\To\\Your Document.pdf"    # Path to your PDF file
tif_dest = "C:\\Path\\To\\Output.tiff"             # Path to your output TIFF file

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

# Use subprocess to execute the command
try:
    subprocess.check_call(cmd)
    print("Ghostscript executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error in Ghostscript execution:", e)
