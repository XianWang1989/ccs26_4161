
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <body>
                <h1 style="color: blue; font-size: 24px;">This is blue and larger text!</h1>
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
