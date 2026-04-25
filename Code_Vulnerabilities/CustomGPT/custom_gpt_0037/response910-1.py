
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
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

    try:
        subprocess.check_call(cmd)
        print("Ghostscript executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing Ghostscript: {}".format(e))

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path\\To\\Input.pdf"
tif_dest = "C:\\Path\\To\\Output.tiff"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
