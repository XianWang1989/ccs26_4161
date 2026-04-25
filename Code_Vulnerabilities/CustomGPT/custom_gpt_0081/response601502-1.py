
from flask import Flask, request, session, redirect, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for demonstration
USER_DATA = {'username': 'test', 'password': 'password'}

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['next_post'] = request.form.to_dict()  # Save the POST data
            flash('You need to log in!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USER_DATA['username'] and password == USER_DATA['password']:
            session['user_id'] = username
            # After login, check if we have any next_post
            next_post = session.get('next_post')
            if next_post:
                return redirect(url_for('handle_post', **next_post))  # Redirect to the target post
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post():
    # Process the data from the POST request
    data = request.form
    return f'Form submitted successfully with data: {data}', 200

@app.route('/form', methods=['GET'])
@login_required
def form():
    return render_template('form.html')

@app.route('/')
def home():
    return 'Welcome! Go to /form to submit your data.'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
