
from flask import Flask, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate-file')
def generate_file():
    # Sample dynamic content creation
    filename = 'dynamic_file.txt'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(filepath, 'w') as file:
        file.write("This is some dynamic content!")

    return f"File created: {filename}"

@app.route('/files/<filename>')
def get_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run()
