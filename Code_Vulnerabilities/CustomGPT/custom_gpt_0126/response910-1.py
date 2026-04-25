
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command with a list
    cmd = [
        ghostscript_path,
        'gswin32c',
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
    output, error = process.communicate()

    if process.returncode != 0:
        print("Error:", error)
    else:
        print("Success:", output)

# Usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path\\To\\Input\\file.pdf"
tif_dest = "C:\\Path\\To\\Output\\file.tiff"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
