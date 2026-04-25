
import subprocess

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Construct the command and arguments as a list
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196X204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),  # Output file
        pdf_source  # Input file
    ]

    # Use subprocess.Popen to execute the command
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()  # Capture output and errors

        if process.returncode != 0:
            print("Error: {}".format(err))
        else:
            print("Output: {}".format(out))
    except Exception as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
tif_dest = 'C:\\Path\\To\\Output\\output.tif'
pdf_source = 'C:\\Path\\To\\Input\\input.pdf'
run_ghostscript(ghostscript_path, tif_dest, pdf_source)
