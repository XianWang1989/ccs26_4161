
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Create the command as a list of arguments
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

    # Use subprocess to execute the command
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

# Example usage
ghostscript_path = "C:\\Program Files\\gs\\gs9.53.3\\bin\\"
pdf_source = '"C:\\path to\\your document.pdf"'  # Make sure to handle spaces in path
tif_dest = '"C:\\output path\\output.tif"'  # Make sure to handle spaces in path

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
