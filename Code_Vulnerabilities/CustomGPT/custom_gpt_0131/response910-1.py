
import subprocess

# Define your paths and command arguments
ghostscript_path = "C:\\path\\to\\ghostscript\\bin\\gswin32c.exe"  # Update this path
tifDest = "C:\\path\\to\\output\\output_image.tiff"  # Update this path
pdfSource = "C:\\path\\to\\input\\input_file.pdf"  # Update this path

# Create the command as a list, which is safer for spaces in paths
command = [
    ghostscript_path,
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196x204",
    "-sPAPERSIZE=a4",
    "-sOutputFile=" + tifDest,
    pdfSource
]

# Execute the command
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing Ghostscript: {e}")
