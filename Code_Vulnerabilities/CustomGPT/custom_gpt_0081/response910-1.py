
import subprocess

# Define your paths and arguments safely
ghostscript_path = 'C:\\Path\\To\\ghostscript\\bin\\gswin32c.exe'  # Adjust the path to your settings
tif_dest = 'C:\\Path\\To\\output\\file.tiff'
pdf_source = 'C:\\Path\\To\\input\\file.pdf'

# Create a command list that includes the executable and arguments
command = [
    ghostscript_path,
    '-q',
    '-dNOPAUSE',
    '-dBATCH',
    '-sDEVICE=tiffg4',
    '-r196x204',
    '-sPAPERSIZE=a4',
    '-sOutputFile={}'.format(tif_dest),  # Format strings to include arguments safely
    pdf_source
]

# Execute the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture output and errors for logging or debugging
stdout, stderr = process.communicate()

# Check for errors
if process.returncode != 0:
    print('Error:', stderr.decode())
else:
    print('Success:', stdout.decode())
