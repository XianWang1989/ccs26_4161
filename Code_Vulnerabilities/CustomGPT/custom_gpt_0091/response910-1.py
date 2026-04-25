
import os

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command with proper quoting
    cmd = [
        os.path.join(ghostscript_path, 'gswin32c.exe'),
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile="%s"' % tif_dest,
        pdf_source
    ]

    # Join the command list into a single string
    cmd_str = ' '.join(cmd)

    # Execute the command
    os.popen(cmd_str)

# Example usage
ghostscript_path = 'C:\\path\\to\\ghostscript'
pdf_source = 'C:\\path\\to\\input file.pdf'
tif_dest = 'C:\\path\\to\\output file.tiff'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
