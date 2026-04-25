
import subprocess

class GhostscriptExecutor:
    def __init__(self, ghostscript_path):
        self._ghostscriptPath = ghostscript_path

    def execute(self, tif_dest, pdf_source):
        # Prepare the command and arguments
        command = [
            self._ghostscriptPath + 'gswin32c',
            '-q',
            '-dNOPAUSE',
            '-dBATCH',
            '-sDEVICE=tiffg4',
            '-r196X204',
            '-sPAPERSIZE=a4',
            '-sOutputFile=' + tif_dest,
            pdf_source
        ]

        # Execute the command
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

# Example usage
ghostscript_executor = GhostscriptExecutor("C:\\Path\\To\\Ghostscript\\")
ghostscript_executor.execute("C:\\Path\\To\\Output.tiff", "C:\\Path\\To\\Input.pdf")
