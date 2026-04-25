
from flask import Flask, request, redirect, session, url_for, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

def login_required(f):
    def wrapped(*args, **kwargs):
        if not session.get('logged_in'):
            session['post_data'] = request.form if request.method == 'POST' else None
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapped

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic...
        session['logged_in'] = True
        post_data = session.pop('post_data', None)

        if post_data:
            return redirect(url_for('protected_route', **post_data))
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected_route():
    data = request.form
    # Handle the POST request
    return jsonify(data)

@app.route('/')
def home():
    return "Welcome to Home Page"

if __name__ == '__main__':
    app.run(debug=True)
