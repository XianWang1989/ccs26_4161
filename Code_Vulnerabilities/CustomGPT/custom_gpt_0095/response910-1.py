
import subprocess

def execute_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Construct the command as a list to avoid issues with spaces in paths
    cmd = [ghostscript_path + 'gswin32c', '-q', '-dNOPAUSE', '-dBATCH', 
           '-sDEVICE=tiffg4', '-r196x204', '-sPAPERSIZE=a4', 
           '-sOutputFile={}'.format(tif_dest), pdf_source]

    # Execute the command
    try:
        subprocess.Popen(cmd)
    except Exception as e:
        print("An error occurred: {}".format(e))

# Example usage
ghostscript_path = "C:\\Program Files\\gs\\gs9.53\\bin\\"
tif_dest = '"C:\\path with spaces\\output.tiff"'
pdf_source = '"C:\\path with spaces\\input.pdf"'
execute_ghostscript(ghostscript_path, tif_dest, pdf_source)
