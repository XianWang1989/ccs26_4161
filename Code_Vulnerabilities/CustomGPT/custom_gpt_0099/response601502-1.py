
from flask import Flask, session, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        # Check if user is logged in
        if not session.get('user_id'):
            # Store original POST data in the session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        # For example, validate user credentials and set session['user_id']
        session['user_id'] = 'some_user_id'  # Replace with actual user ID
        flash('Logged in successfully!')

        # Check if there's any post data to handle
        if 'post_data' in session:
            # Extract the post data
            post_data = session.pop('post_data')  # Remove from session

            # Perform the original POST request handling
            return handle_post_request(post_data)

        return redirect(url_for('home'))  # Redirect to a home page after login

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request normally if logged in
    return "This is a protected POST request."

def handle_post_request(post_data):
    # Simulate processing the stored POST data
    return f"Processed data: {post_data}"

@app.route('/')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
