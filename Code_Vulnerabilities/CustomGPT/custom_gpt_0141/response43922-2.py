
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Using HTML and inline CSS to style the text
    return render_template_string('''
        <html>
            <head>
                <style>
                    .blue-text {
                        color: blue;
                        font-size: 24px; /* Increase font size */
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
