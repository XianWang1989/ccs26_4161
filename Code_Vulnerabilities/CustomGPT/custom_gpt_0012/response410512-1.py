
from flask import Flask, request
from itsdangerous import URLSafeTimedSerializer
import os

app = Flask(__name__)
secret_key = os.urandom(24)
serializer = URLSafeTimedSerializer(secret_key)

@app.route('/get_file/<filename>')
def get_file(filename):
    # Logic to serve the file
    return send_from_directory('your_directory', filename)

@app.route('/generate_link/<filename>')
def generate_link(filename):
    # Generate a signed URL that will expire after 600 seconds
    token = serializer.dumps(filename)
    link = f"http://yourdomain.com/get_file/{token}"
    return {'url': link}

@app.route('/get_file/<token>')
def send_file(token):
    try:
        # Verify token and extract the filename
        filename = serializer.loads(token, max_age=600)
        return get_file(filename)
    except Exception:
        return "Link expired or invalid", 404

if __name__ == '__main__':
    app.run()
