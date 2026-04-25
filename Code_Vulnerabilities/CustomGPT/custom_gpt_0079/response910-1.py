
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
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

    try:
        subprocess.Popen(cmd)
    except OSError as e:
        print("Error executing command:", e)

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path\\To\\Input.pdf"
tif_dest = "C:\\Path\\To\\Output.tif"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
