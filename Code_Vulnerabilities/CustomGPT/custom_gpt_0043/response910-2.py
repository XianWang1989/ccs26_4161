
import subprocess

# Use subprocess.run or subprocess.call (in Python 3)
result = subprocess.run([ghostscript_path, '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=tiffg4',
                         '-r196X204', '-sPAPERSIZE=a4', '-sOutputFile={}'.format(tif_dest), pdf_source],
                        check=True)
