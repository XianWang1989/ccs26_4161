
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Create the command as a list
    cmd = [
        ghostscript_path + 'gswin32c',
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile=' + tif_dest,
        pdf_source
    ]

    # Execute the command
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError as e:
        print("An error occurred: ", e)

# Example usage
execute_ghostscript('C:\\Path\\To\\Ghostscript\\', 'C:\\Path\\To\\Input.pdf', 'C:\\Path\\To\\Output.tif')
