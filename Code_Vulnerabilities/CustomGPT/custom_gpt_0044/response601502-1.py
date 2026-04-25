
from flask import Flask, redirect, request, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user login
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
        # Here would be your login logic
        session['user_id'] = 'example_user_id'
        flash("Logged in successfully!")

        # Check if there was any stored POST request data
        if 'post_data' in session:
            post_data = session.pop('post_data')  # Get and remove the data from session
            return handle_post_request(post_data)  # Reprocess the stored request
        return redirect(url_for('some_page'))  # Redirect elsewhere

    return 'Login Form Here'  # Your login form HTML

@app.route('/some_post', methods=['POST'])
@login_required
def handle_post_request():
    # Normal processing of the post request
    data = request.form
    return f"Handled POST request with data: {data}"

@app.route('/some_page')
def some_page():
    return "This is some page."

if __name__ == '__main__':
    app.run(debug=True)
