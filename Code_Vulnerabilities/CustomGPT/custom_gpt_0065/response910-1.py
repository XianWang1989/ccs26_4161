
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Prepare the command and arguments
    command = [
        ghostscript_path + 'gswin32c',  # Ghostscript executable
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile=' + tif_dest,
        pdf_source
    ]

    # Execute the command
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print("Error executing Ghostscript:", e)

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path\\To\\Source\\document.pdf"
tif_dest = "C:\\Path\\To\\Output\\output.tif"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
