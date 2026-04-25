
import subprocess

# Define the paths and arguments
ghostscript_path = self._ghostscriptPath
tif_dest = "path/to/output.tif"  # Replace with your output path
pdf_source = "path/to/source.pdf"  # Replace with your PDF source path

# Construct the command as a list
cmd = [
    ghostscript_path + 'gswin32c',
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196X204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),
    pdf_source
]

# Execute the command
subprocess.run(cmd)
