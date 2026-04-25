
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Define the command and arguments as a list
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
    try:
        subprocess.call(cmd)
        print("Ghostscript executed successfully.")
    except Exception as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = "C:\\Program Files\\gs\\gs9.54\\bin\\"
pdf_source = '"C:\\path to\\input file.pdf"'  # Ensure paths are quoted
tif_dest = '"C:\\path to\\output file.tif"'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
