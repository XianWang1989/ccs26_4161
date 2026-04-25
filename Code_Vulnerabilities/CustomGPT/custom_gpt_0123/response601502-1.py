
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store POST data for after login
            session['post_data'] = request.form.to_dict()
            flash('Please log in to access that page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['user_id'] = 'user_id_value'  # Set user_id after successful login
        post_data = session.pop('post_data', None)
        if post_data:
            # Reissue POST request using stored data
            return handle_post_request(post_data)
        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post_request():
    # Handle your POST request logic here
    return 'POST request handled!'

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
