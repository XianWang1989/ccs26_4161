
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <html>
    <head>
        <style>
            .blue-text {
                color: blue;
                font-size: 24px; /* Bigger text */
            }
        </style>
    </head>
    <body>
        <p class="blue-text">This text is blue and bigger!</p>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
