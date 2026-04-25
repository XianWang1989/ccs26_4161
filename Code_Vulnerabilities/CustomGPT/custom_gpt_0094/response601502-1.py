
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Dummy user authentication check
def is_authenticated():
    return 'user' in session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store request details before redirecting to login
            session['original_request'] = {
                'method': request.method,
                'url': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user is authenticated after this
        session['user'] = 'some_user'  # Simulate user login
        original_request = session.pop('original_request', None)

        if original_request:
            # Redirect accordingly after logging in
            return handle_post_request(original_request)

    return '<form method="post">Login</form>'

def handle_post_request(original_request):
    # Manually call the view function (e.g., /some-endpoint)
    if original_request['url'] == '/some-endpoint':
        return some_endpoint(original_request['form_data'])
    return 'No original request found.'

@app.route('/some-endpoint', methods=['POST'])
@login_required
def some_endpoint():
    data = request.form
    # Process the data
    return f"Data processed: {data}"

if __name__ == '__main__':
    app.run(debug=True)
