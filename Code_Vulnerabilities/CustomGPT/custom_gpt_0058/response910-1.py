
import subprocess

# Define the Ghostscript command and arguments as a list
ghostscript_command = [
    "gswin32c",
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    "-sOutputFile={}".format(tifDest),  # "{}" allows safe formatting
    pdfSource
]

# Use subprocess.Popen to execute the command
try:
    process = subprocess.Popen(ghostscript_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()  # Capture the output and error
    print(stdout)  # Print standard output
    if stderr:
        print("Error:", stderr)  # Print any errors
except OSError as e:
    print("Execution failed:", e)
