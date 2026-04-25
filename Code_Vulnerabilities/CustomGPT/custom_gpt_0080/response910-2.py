
import os

cmd = (
    '"{}" -q -dNOPAUSE -dBATCH -sDEVICE=tiffg4 -r196X204 '
    '-sPAPERSIZE=a4 -sOutputFile="{}" "{}"'
).format(ghostscript_path, tif_dest, pdf_source)

os.system(cmd)
