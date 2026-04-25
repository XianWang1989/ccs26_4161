
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command as a list of arguments
    cmd = [
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
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Error:", stderr)
    else:
        print("Success:", stdout)

# Example usage
ghostscript_path = 'C:\\Program Files\\gs\\gs9.54\\bin\\'  # Adjust path as necessary
pdf_source = 'C:\\path with spaces\\input.pdf'
tif_dest = 'C:\\path with spaces\\output.tiff'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
