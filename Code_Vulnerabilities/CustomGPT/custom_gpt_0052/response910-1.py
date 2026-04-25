
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command as a list
    command = [
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
    try:
        subprocess.check_call(command)
        print("Ghostscript executed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

# Usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\'  # Update with your path
pdf_source = 'C:\\Path With Spaces\\source.pdf'
tif_dest = 'C:\\Path With Spaces\\output.tif'

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
