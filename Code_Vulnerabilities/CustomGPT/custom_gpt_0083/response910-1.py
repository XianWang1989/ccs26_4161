
import subprocess

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Construct the command as a list
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Execute the command
    subprocess.Popen(cmd)

# Example usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'
tif_dest = 'C:\\Path\\To\\Output\\output.tif'
pdf_source = 'C:\\Path\\To\\Input\\input.pdf'

run_ghostscript(ghostscript_path, tif_dest, pdf_source)
