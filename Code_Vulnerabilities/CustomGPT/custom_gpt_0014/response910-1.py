
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Prepare the command and arguments as a list
    command = [
        ghostscript_path,  # Path to Ghostscript executable
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
    subprocess.call(command)

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path\\To\\Source\\file.pdf"
tif_dest = "C:\\Path\\To\\Destination\\output.tif"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
