
from flask import Flask, session, redirect, url_for, request, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['original_url'] = request.path
            session['form_data'] = request.form.to_dict()  # Store form data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate a login action
        session['logged_in'] = True
        flash('You were logged in!')

        # If there was an original URL, redirect to it
        original_url = session.pop('original_url', None)
        form_data = session.pop('form_data', None)

        if original_url and form_data:
            # Call the original POST request handler
            return execute_post(original_url, form_data)

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Actual handling of the POST request
    data = request.form
    return f"Data received: {data}"

def execute_post(original_url, form_data):
    with app.test_request_context(original_url, method='POST', data=form_data):
        return post_endpoint()

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
