
from flask import Flask, request, redirect, url_for, session, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user login check
def is_logged_in():
    return 'user_id' in session

# Custom decorator to check login status
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store the POST data in the session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Login route (illustrative purposes)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user (mockup)
        session['user_id'] = 'authenticated_user'
        flash('Login successful!')

        # Execute the previously stored POST request if available
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(url_for(post_data['target']), **post_data)

        return redirect(url_for('home'))

    return render_template('login.html')

# Example POST route
@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # This will execute only if logged in
    data = request.form
    # Process the data...
    return f"Data submitted: {data}"

@app.route('/')
def home():
    return "Welcome to the homepage!"

if __name__ == '__main__':
    app.run(debug=True)
