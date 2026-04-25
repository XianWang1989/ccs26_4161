
from flask import Flask, request, redirect, session, url_for, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login check function
def is_logged_in():
    return 'user_id' in session

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store original path and POST data
            session['original_path'] = request.path
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle login logic here and set session user_id if successful
        session['user_id'] = 'some_user_id'  # Replace with actual user check and ID

        # After login, check if there's original data to process
        original_path = session.pop('original_path', None)
        original_data = session.pop('original_data', None)

        if original_path and original_data:
            return redirect(original_path, code=307)  # Use 307 to preserve the method
        return redirect(url_for('home'))  # Redirect to a default page

    return render_template('login.html')  # Render login page

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request here
    data = request.form
    return f"Data received: {data}"

@app.route('/')
def home():
    return "Welcome! You can go to /post-endpoint."

if __name__ == '__main__':
    app.run(debug=True)
