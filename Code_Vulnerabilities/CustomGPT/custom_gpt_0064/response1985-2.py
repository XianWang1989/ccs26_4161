
from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 30, 22]
    }
    df = pd.DataFrame(data)

    # Convert to HTML
    html_output = df.to_html(index=False)

    return render_template_string(html_output)

if __name__ == '__main__':
    app.run(debug=True)
