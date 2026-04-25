
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

    # Execute the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Error:", stderr)
    else:
        print("Success:", stdout)

# Example usage
execute_ghostscript('C:\\Path\\To\\Ghostscript\\', 'C:\\Path\\To\\Input.pdf', 'C:\\Path\\To\\Output.tif')
