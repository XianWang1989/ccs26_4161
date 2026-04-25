
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user_id'] = 'authenticated_user'  # Simplified login
        flash('Logged in successfully.')

        # Check if there's original POST data
        post_data = session.get('post_data')
        if post_data:
            # Directly make the POST request for the original endpoint
            # Here you would typically redirect to that endpoint instead
            session.pop('post_data')  # Clear post_data after using it
            return redirect(url_for('post_route', **post_data))

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post', methods=['POST'])
@login_required
def post_route():
    # Handle the POST request
    return 'Post request processed!'

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
