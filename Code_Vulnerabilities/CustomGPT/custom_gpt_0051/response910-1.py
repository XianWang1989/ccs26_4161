
import os

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Construct the command with quotes for paths that contain spaces
    cmd = (
        '\"{}gswin32c\" -q -dNOPAUSE -dBATCH -sDEVICE=tiffg4 '
        '-r196X204 -sPAPERSIZE=a4 -sOutputFile=\"{}\" \"{}\"'
    ).format(ghostscript_path, tif_dest, pdf_source)

    # Execute the command
    os.popen(cmd)

# Example usage
ghostscript_path = "C:\\Program Files\\gs\\gs9.50\\bin\\"
tif_dest = "C:\\output\\image.tif"
pdf_source = "C:\\input\\document.pdf"

run_ghostscript(ghostscript_path, tif_dest, pdf_source)
