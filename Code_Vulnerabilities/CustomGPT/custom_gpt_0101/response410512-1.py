
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/dynamic_media/<filename>')
def dynamic_media(filename):
    # Logic to generate or retrieve the file
    file_path = f"/path/to/media/{filename}"  # Adjust as necessary
    return redirect(url_for('serve_file', filepath=file_path))

@app.route('/serve_file/<path:filepath>')
def serve_file(filepath):
    return send_from_directory('/path/to/media', filepath)

if __name__ == '__main__':
    app.run()
