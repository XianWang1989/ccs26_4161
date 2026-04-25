
import subprocess

def execute_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Prepare the command as a list of arguments
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile=' + tif_dest,
        pdf_source
    ]

    # Use subprocess.call to execute the command
    subprocess.call(cmd)

# Example usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'  # Ensure this path is correct
tif_dest = 'C:\\Path\\To\\Output\\output.tiff'
pdf_source = 'C:\\Path\\To\\Input\\input.pdf'

execute_ghostscript(ghostscript_path, tif_dest, pdf_source)
