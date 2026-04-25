
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['original_request'] = {
                'method': request.method,
                'url': request.url,
                'form_data': request.form.to_dict(),
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user (implement your logic here)
        session['user_id'] = 'some_user_id'  # Example user_id

        # After logging in, check for a stored request
        if 'original_request' in session:
            original_request = session.pop('original_request')
            return redirect(original_request['url'])

    return 'Login Page'

@app.route('/api/some-protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    # Process your original POST request
    data = request.form  # Access the original form data
    return f"Received data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
