
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/generate/<filename>')
def generate_file(filename):
    # Simulate dynamic file generation
    file_path = f'/tmp/{filename}'
    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Instead of returning the file directly, just indicate where it is
    return {"message": f"File generated at /tmp/{filename}. You can download it from Nginx."}

@app.route('/download/<filename>')
def download_file(filename):
    # Serve the file using send_file()
    file_path = f'/tmp/{filename}'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
