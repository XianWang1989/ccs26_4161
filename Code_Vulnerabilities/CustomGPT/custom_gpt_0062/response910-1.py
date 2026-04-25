
import os
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Create the command as a list of arguments
    cmd = [
        os.path.join(ghostscript_path, 'gswin32c'),
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Execute the command
    try:
        subprocess.Popen(cmd, shell=False)
    except Exception as e:
        print("Error executing command: {}".format(e))

# Example usage
ghostscript_path = r'C:\Path\To\Ghostscript'
pdf_source = r'C:\Path\To\Your PDF.pdf'
tif_dest = r'C:\Path\To\Output\Image.tif'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
