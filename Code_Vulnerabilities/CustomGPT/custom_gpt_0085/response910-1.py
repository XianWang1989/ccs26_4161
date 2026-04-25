
import subprocess

def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command and arguments as a list
    cmd = [
        ghostscript_path, 
        "gswin32c", 
        "-q", 
        "-dNOPAUSE", 
        "-dBATCH", 
        "-sDEVICE=tiffg4", 
        "-r196X204", 
        "-sPAPERSIZE=a4", 
        "-sOutputFile={}".format(tif_dest), 
        pdf_source
    ]

    # Execute the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Handle output and errors
    if process.returncode == 0:
        print("Success:", stdout)
    else:
        print("Error:", stderr)

# Example usage
ghostscript_path = "C:\\Path\\To\\Ghostscript\\"
pdf_source = "C:\\Path With Spaces\\file.pdf"
tif_dest = "C:\\Output Path\\file.tiff"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
