
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/media/<filename>')
def media(filename):
    file_path = os.path.join('./media', filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
