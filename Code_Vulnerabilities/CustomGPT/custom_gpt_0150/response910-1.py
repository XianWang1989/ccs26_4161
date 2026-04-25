
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command with proper quoting
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile=' + '"' + tif_dest + '"',
        '"' + pdf_source + '"'
    ]

    # Run the command
    subprocess.Popen(cmd, shell=True)

# Example usage
run_ghostscript('C:\\Path\\To\\Ghostscript\\', 'C:\\Path With Spaces\\input.pdf', 'C:\\Output\\output.tif')
