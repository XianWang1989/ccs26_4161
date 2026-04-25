
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''<html>
    <body>
        <p style="color: blue; font-size: 20px;">This is blue and bigger text!</p>
    </body>
    </html>''')

if __name__ == '__main__':
    app.run(debug=True)
