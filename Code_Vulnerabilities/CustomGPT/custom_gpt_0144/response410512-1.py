from flask import Flask, redirect, url_for
import os
import uuid

app = Flask(__name__)
DYNAMIC_MEDIA_DIR = "/tmp/dynamic_media"  # Nginx will serve from here
URL_PREFIX = "/media"  # URL to be served by Nginx

os.makedirs(DYNAMIC_MEDIA_DIR, exist_ok=True)

@app.route('/generate')
def generate_file():
    content = "This is dynamic content."
    filename = f"{uuid.uuid4()}.txt"
    filepath = os.path.join(DYNAMIC_MEDIA_DIR, filename)

    with open(filepath, 'w') as f:
        f.write(content)

    # Redirect to URL served by Nginx
    return redirect(f"{URL_PREFIX}/{filename}")
