
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

    subprocess.call(cmd)

# Example usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'
pdf_source = 'C:\\Path\\To\\Source\\file.pdf'
tif_dest = 'C:\\Path\\To\\Dest\\file.tiff'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
