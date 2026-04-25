import os
import subprocess
import sys
import tempfile
import time

def update_application(installer_path):
    # Create a temporary batch file
    temp_dir = tempfile.mkdtemp()
    batch_file = os.path.join(temp_dir, 'update_launcher.bat')

    with open(batch_file, 'w') as f:
        f.write(f"""
        @echo off
        :waitloop
        tasklist | findstr /I "{os.path.basename(sys.argv[0])}"
        if not errorlevel 1 (
            timeout /t 1 /nobreak >nul
            goto waitloop
        )
        start "" "{installer_path}" /SP- /silent /noicons /nocancel /password="pw"
        """)

    # Launch the batch file
    subprocess.Popen(
        [batch_file],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    # Exit the main application
    sys.exit()

# Example usage
installer_path = os.path.join(os.getcwd(), 'update_myprog.exe')
update_application(installer_path)
