
import subprocess

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command and arguments as a list
    command = [
        ghostscript_path + 'gswin32c',
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
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Error occurred: ", stderr)
    else:
        print("Success: ", stdout)

# Example usage
ghostscript_path = "C:\\path\\to\\ghostscript\\bin\\"
pdf_source = "C:\\path\\to\\your\\input.pdf"  # Example path with spaces
tif_dest = "C:\\path\\to\\your\\output.tif"   # Example path with spaces

run_ghostscript(ghostscript_path, pdf_source, tif_dest)
