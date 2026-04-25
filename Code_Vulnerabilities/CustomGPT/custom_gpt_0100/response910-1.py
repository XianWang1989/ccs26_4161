
import subprocess

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Construct the command as a list of arguments
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Execute the command
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("An error occurred: {}".format(e))

# Example usage
run_ghostscript("C:\\Path\\To\\Ghostscript\\", "output.tiff", "input.pdf")
