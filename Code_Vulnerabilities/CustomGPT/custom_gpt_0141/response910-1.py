
import os
import shlex  # Note: shlex is not available in Python 2.3. This is for demonstration only.

# Example function to call Ghostscript
def execute_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Construct the command components
    cmd = [
        os.path.join(ghostscript_path, 'gswin32c'),  # Path to Ghostscript executable
        '-q', 
        '-dNOPAUSE', 
        '-dBATCH', 
        '-sDEVICE=tiffg4', 
        '-r196X204', 
        '-sPAPERSIZE=a4', 
        '-sOutputFile={}'.format(tif_dest), 
        pdf_source  # The input PDF file
    ]

    # Join the command with spaces and ensure paths are safely quoted
    cmd_string = ' '.join(cmd)

    # Print command for debugging purposes
    print("Executing command:", cmd_string)

    # Execute the command
    os.popen(cmd_string)  # Consider using subprocess in Python 2.4 or newer

# Example usage
ghostscript_path = r"C:\Program Files\gs\gs9.53.3\bin"  # Adjust your path as necessary
pdf_source = r"C:\path\to\source.pdf"
tif_dest = r"C:\path\to\output.tif"

execute_ghostscript(ghostscript_path, pdf_source, tif_dest)
