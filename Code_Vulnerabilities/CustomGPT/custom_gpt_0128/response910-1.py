
import os
import shlex

def run_ghostscript(ghostscript_path, pdf_source, tif_dest):
    # Command components
    command = [
        os.path.join(ghostscript_path, 'gswin32c.exe'),
        '-q',
        '-dNOPAUSE',
        '-dBATCH',
        '-sDEVICE=tiffg4',
        '-r196x204',
        '-sPAPERSIZE=a4',
        '-sOutputFile={}'.format(tif_dest),
        pdf_source
    ]

    # Join the command using shlex to handle spaces appropriately
    cmd = ' '.join(command)

    # Execute the command
    os.system(cmd)

# Example usage
run_ghostscript('C:\\Path\\To\\Ghostscript\\bin', 'C:\\Path To\\Input.pdf', 'C:\\Path To\\Output.tif')
