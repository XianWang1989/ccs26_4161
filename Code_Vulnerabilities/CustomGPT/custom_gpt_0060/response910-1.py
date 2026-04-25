
import os
import sys

def run_ghostscript(ghostscript_path, tif_dest, pdf_source):
    # Prepare the command and arguments
    command = os.path.join(ghostscript_path, 'gswin32c')
    args = [
        command,
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Spawn the process
    pid = os.spawnv(os.P_WAIT, command, args)

    if pid == -1:
        print("Error executing Ghostscript")
    else:
        print("Ghostscript executed successfully, PID:", pid)

# Example usage
ghostscript_path = 'C:\\Path\\To\\Ghostscript\\bin'
tif_dest = 'C:\\Path\\To\\Output\\output.tif'
pdf_source = 'C:\\Path\\To\\Input\\input.pdf'
run_ghostscript(ghostscript_path, tif_dest, pdf_source)
