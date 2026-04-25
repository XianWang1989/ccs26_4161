
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command as a list of arguments
    cmd = [
        ghostscript_path + 'gswin32c.exe',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile=' + tif_dest,
        pdf_source
    ]

    # Execute the command
    subprocess.call(cmd)

# Example usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'  # Update this with your actual Ghostscript path
pdf_source = 'C:\\Path With Spaces\\source.pdf'
tif_dest = 'C:\\Path With Spaces\\destination.tif'

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
