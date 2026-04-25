
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Build the command as a list
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
    subprocess.Popen(cmd)

# Example usage
run_ghostscript('C:\\path\\to\\ghostscript\\', 'C:\\path\\to\\source.pdf', 'C:\\path\\to\\output.tif')
