
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data in the session
            session['post_data'] = request.form.to_dict()
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user_id'] = 'user_id_value'  # Set user_id after successful login
        flash('Logged in successfully.')

        # Check if there's post data to process
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(url_for(post_data['url'], **post_data))

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the post request
    data = request.form
    # Process the data
    return 'Post request processed!'

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
