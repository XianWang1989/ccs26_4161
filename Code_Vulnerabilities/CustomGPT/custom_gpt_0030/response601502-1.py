
from flask import Flask, request, session, redirect, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user authentication for demonstration
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original path and POST data
            session['original_url'] = request.url
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform authentication (example logic)
        session['user_id'] = 'authenticated_user'
        flash("Successfully logged in!")

        # After login, check if there was a pending POST request
        if 'original_url' in session and 'post_data' in session:
            original_url = session.pop('original_url')
            post_data = session.pop('post_data')
            return handle_post_request(original_url, post_data)

        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Process the POST request
    return "Post Request Processed"

def handle_post_request(original_url, post_data):
    # Here you can call the function directly or reprocess the data
    # For demonstration, we will simply return the processed data
    return f"Re-executed POST to {original_url} with data: {post_data}"

@app.route('/')
def home():
    return "Welcome to Home!"

if __name__ == '__main__':
    app.run(debug=True)
