
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

    # Execute the command
    subprocess.call(cmd)

# Usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'
pdf_source = 'C:\\Path\\To\\file.pdf'
tif_dest = 'C:\\Path\\To\\output.tiff'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
