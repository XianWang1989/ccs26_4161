
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''
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
        <p class="blue-text">This text is blue and larger!</p>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
