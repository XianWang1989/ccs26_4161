
import os

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Quote paths that may contain spaces
    pdf_source = '"{}"'.format(pdf_source)
    tif_dest = '"{}"'.format(tif_dest)

    cmd = '{}gswin32c -q -dNOPAUSE -dBATCH -sDEVICE=tiffg4 -r196x204 -sPAPERSIZE=a4 -sOutputFile={} {}'.format(
        ghostscript_path, tif_dest, pdf_source
    )

    # Execute the command
    os.popen(cmd)

# Example usage
ghostscript_path = 'C:/Path/To/Ghostscript/'
pdf_source = 'C:/Path/To/Sample File.pdf'
tif_dest = 'C:/Path/To/Output File.tiff'

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
