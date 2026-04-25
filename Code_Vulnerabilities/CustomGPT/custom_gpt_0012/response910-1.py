
import subprocess

class GhostscriptExecutor:
    def __init__(self, ghostscript_path):
        self.ghostscript_path = ghostscript_path

    def execute(self, pdf_source, tif_dest):
        command = [
            self.ghostscript_path + 'gswin32c',  # Ghostscript executable
            '-q',                                   # Suppress output
            '-dNOPAUSE',                            # No pause
            '-dBATCH',                              # Batch mode
            '-sDEVICE=tiffg4',                     # Output device
            '-r196X204',                           # Resolution
            '-sPAPERSIZE=a4',                      # Paper size
            '-sOutputFile=' + tif_dest,            # Output file
            pdf_source                              # Input file
        ]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f'Successfully converted {pdf_source} to {tif_dest}')
        except subprocess.CalledProcessError as e:
            print(f'An error occurred: {e}')

# Example usage:
gs_executor = GhostscriptExecutor('C:/Path/To/Ghostscript/')
gs_executor.execute('C:/Path/To/Input.pdf', 'C:/Path/To/Output.tiff')
