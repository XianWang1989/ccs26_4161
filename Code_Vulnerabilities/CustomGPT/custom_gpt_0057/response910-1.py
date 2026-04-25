
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
        '-sOutputFile={0}'.format(tif_dest),
        pdf_source
    ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Error executing Ghostscript:")
        print(stderr)
    else:
        print("Ghostscript executed successfully:")
        print(stdout)

# Example usage (replace with actual paths):
# execute_ghostscript('C:\\Path\\To\\Ghostscript\\', 'C:\\Path\\To\\input.pdf', 'C:\\Path\\To\\output.tiff')
