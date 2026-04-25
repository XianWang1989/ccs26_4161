
from flask import Flask, send_file
import os

app = Flask(__name__)
output_dir = 'static/files'  # Directory to save dynamic files

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

@app.route('/generate/<filename>', methods=['GET'])
def generate_file(filename):
    # Create dynamic content (as an example)
    content = f"This is the dynamically generated content for {filename}"
    file_path = os.path.join(output_dir, filename)

    # Write the content to a file
    with open(file_path, 'w') as f:
        f.write(content)

    return f"File {filename} generated successfully. You can access it at /files/{filename}"

if __name__ == "__main__":
    app.run()
