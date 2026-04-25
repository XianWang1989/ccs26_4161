import os

GHOSTSCRIPT_PATH = "C:\\Path To\\Ghostscript\\bin\\gswin32c.exe"
tifDest = "C:\\Output Folder\\output.tif"
pdfSource = "C:\\Documents\\input.pdf"

args = [
    "gswin32c",
    "-q",
    "-dNOPAUSE",
    "-dBATCH",
    "-sDEVICE=tiffg4",
    "-r196X204",
    "-sPAPERSIZE=a4",
    '-sOutputFile=' + tifDest,
    pdfSource
]

# os.P_WAIT makes it wait for the command to complete
os.spawnv(os.P_WAIT, GHOSTSCRIPT_PATH, [GHOSTSCRIPT_PATH] + args)
