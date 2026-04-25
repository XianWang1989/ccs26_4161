
import subprocess

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Define the command and arguments
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),  # Use .format for paths
        pdf_source
    ]

    # Execute the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()  # Get output and error messages

    if process.returncode != 0:
        print("Error executing Ghostscript: {}".format(stderr))
    else:
        print("Successfully executed Ghostscript")

# Example usage
ghostscript_path = "C:\\Program Files\\gs\\gs9.50\\bin\\"
tif_dest = r"C:\output\yourfile.tiff"
pdf_source = r"C:\input\yourfile.pdf"

run_ghostscript(ghostscript_path, tif_dest, pdf_source)
