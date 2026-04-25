
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
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

    # Run the command
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("Error occurred: {}".format(e))

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path With Spaces\\source.pdf"
tif_dest = "C:\\Path With Spaces\\output.tif"

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
