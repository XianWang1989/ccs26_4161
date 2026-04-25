
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command using a list for arguments
    command = [
        ghostscript_path + 'gswin32c',
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
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print("An error occurred: ", e)

# Example usage
ghostscript_path = r'C:\Path\To\Ghostscript\'
pdf_source = r'C:\Path\To\Source.pdf'
tif_dest = r'C:\Path\To\Output.tif'

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
