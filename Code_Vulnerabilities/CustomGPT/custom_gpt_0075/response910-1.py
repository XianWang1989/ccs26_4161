
import subprocess

def execute_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Create the command as a list of arguments
    cmd = [
        ghostscript_path,
        'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    try:
        # Execute the command
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

# Example usage
ghostscript_path = r"C:\path\to\ghostscript\"
tif_dest = r"C:\path\to\output\image.tif"
pdf_source = r"C:\path\to\input\document.pdf"
execute_ghostscript(ghostscript_path, tif_dest, pdf_source)
