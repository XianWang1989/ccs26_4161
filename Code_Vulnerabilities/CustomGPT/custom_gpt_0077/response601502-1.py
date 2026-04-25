
from flask import Flask, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login check
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'logged_in' not in session:
            # Store details to be used after login
            if request.method == 'POST':
                session['original_post'] = request.form.to_dict()
                session['original_path'] = request.path
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__  # Preserve function name
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        session['logged_in'] = True
        flash("Login successful!")

        # After login, check for stored POST data
        if 'original_post' in session:
            post_data = session.pop('original_post')
            return redirect(url_for(session.pop('original_path'), **post_data))

        return redirect(url_for('home'))  # Redirect to a home or dashboard after login

    return "<form method='POST'>Login Form</form>"

@app.route('/some_post_endpoint', methods=['POST'])
@login_required
def some_post_handler():
    # Handle the POST request
    return "POST request successful!"

@app.route('/')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
