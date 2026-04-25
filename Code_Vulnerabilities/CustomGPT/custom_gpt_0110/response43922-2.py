
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
        <head>
            <style>
                .big-blue { font-size: 24px; color: blue; }
            </style>
        </head>
        <body>
            <p class="big-blue">This text is big and blue!</p>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
