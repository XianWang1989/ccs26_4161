
import subprocess

# Define your Ghostscript path, input PDF path, and output TIFF path
ghostscript_path = "C:\\Path\\To\\Ghostscript\\gswin32c.exe"  # Adjust this path as needed
pdf_source = 'C:\\Path\\To\\Your\\Document.pdf'  # Path to your PDF file
tif_dest = 'C:\\Path\\To\\Output\\OutputFile.tiff'  # Desired path for output TIFF file

# Build the command as a list
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
    subprocess.call(cmd)
except Exception as e:
    print("An error occurred: {}".format(e))
