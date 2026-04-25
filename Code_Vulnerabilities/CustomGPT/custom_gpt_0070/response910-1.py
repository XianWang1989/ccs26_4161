
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Prepare the command and arguments
    cmd = [
        ghostscript_path + 'gswin32c',  # Path to Ghostscript executable
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),  # Output file
        pdf_source  # Input PDF file
    ]

    # Execute the command
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = r"C:\Path\To\Ghostscript\"  # Adjust the path
pdf_source = r"C:\Path\To\Your\file.pdf"
tif_dest = r"C:\Path\To\Output\file.tiff"

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
