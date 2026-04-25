
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command with a list
    command = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),  # Handle paths directly
        pdf_source
    ]

    # Use subprocess to execute the command
    try:
        result = subprocess.call(command)
        if result == 0:
            print("Ghostscript ran successfully.")
        else:
            print("Ghostscript failed with code:", result)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
ghostscript_path = r'C:\path\to\ghostscript\bin\'
pdf_source = r'C:\path\to\file.pdf'
tif_dest = r'C:\path\to\output.tif'

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
