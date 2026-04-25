
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command with arguments
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

    # Use subprocess to execute the command
    try:
        subprocess.call(cmd, shell=True)
    except Exception as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path With Spaces\\input.pdf"
tif_dest = "C:\\Path With Spaces\\output.tif"
run_ghostscript(ghostscript_path, pdf_source, tif_dest)
