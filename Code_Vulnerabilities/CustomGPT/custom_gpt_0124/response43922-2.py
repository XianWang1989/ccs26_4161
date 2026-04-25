
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string('''
        <html>
            <head>
                <style>
                    .big-text { font-size: 24px; color: blue; }
                </style>
            </head>
            <body>
                <p class="big-text">This text is blue and bigger!</p>
            </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
