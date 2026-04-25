
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Craft the command and arguments
    cmd = [
        ghostscript_path + "gswin32c",
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Use subprocess to execute the command
    try:
        subprocess.check_call(cmd)
        print("Ghostscript executed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = r"C:\Path\To\Ghostscript\"
pdf_source = r"C:\Path With Spaces\file.pdf"
tif_dest = r"C:\Path With Spaces\output.tif"

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
