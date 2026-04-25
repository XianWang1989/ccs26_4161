
from flask import Flask, Response

app = Flask(__name__)

@app.route('/dynamic/<filename>')
def dynamic_content(filename):
    # Dynamically generate content here (e.g., image, video, etc.)
    def generate():
        with open(f'/path/to/media/{filename}', 'rb') as f:
            while chunk := f.read(4096):
                yield chunk

    return Response(generate(), content_type='application/octet-stream')

if __name__ == '__main__':
    app.run()
