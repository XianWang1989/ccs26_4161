
from flask import Flask
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Example: Create a dynamic file
    file_path = 'static/media/my_dynamic_file.txt'
    with open(file_path, 'w') as f:
        f.write('This is dynamic content.')

    return f'File generated: <a href="/media/my_dynamic_file.txt">Download here</a>'

if __name__ == '__main__':
    app.run()
