
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('dynamic_content', filename)
    # Serve the file using nginx or uWSGI
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
