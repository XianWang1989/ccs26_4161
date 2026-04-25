
import subprocess

# Define paths
ghostscript_path = self._ghostscriptPath + 'gswin32c'
pdf_source = pdfSource  # Path to the PDF file
tif_dest = tifDest      # Destination for the TIFF file

# Construct command and arguments
args = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile=' + tif_dest,
    pdf_source
]

# Execute the command
subprocess.call(args)
