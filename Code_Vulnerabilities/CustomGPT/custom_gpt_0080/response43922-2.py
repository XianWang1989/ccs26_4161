
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <html>
        <head>
            <style>
                .big { font-size: 24px; }
                .blue { color: blue; }
            </style>
        </head>
        <body>
            <p class="big blue">This text is blue and bigger!</p>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
