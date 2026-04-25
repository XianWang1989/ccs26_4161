
from flask import Flask, request, session, redirect, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication check
def is_logged_in():
    return 'user_id' in session

# Decorator to protect routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store the request method and form data
            session['requested_url'] = request.url
            session['request_method'] = request.method
            session['form_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume a login function that validates user credentials
        session['user_id'] = 'some_user_id'
        flash('Logged in successfully!')

        # Handle potential stored post request
        if 'requested_url' in session:
            requested_url = session.pop('requested_url')
            request_method = session.pop('request_method')
            form_data = session.pop('form_data', {})

            if request_method == 'POST':
                # Simulate redirect to original POST request
                return handle_post_request(requested_url, form_data)

        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/some_protected_post', methods=['POST'])
@login_required
def some_protected_post():
    return 'This is a protected POST request that was executed successfully!'

def handle_post_request(url, form_data):
    # Here you would extract the endpoint and call the respective function
    with app.test_request_context(url, method='POST', data=form_data):
        response = some_protected_post()
        return response

@app.route('/')
def index():
    return 'Welcome to the index page!'

if __name__ == '__main__':
    app.run(debug=True)
