
from flask import Flask, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Store the request details
            session['original_request'] = {
                'path': request.path,
                'method': request.method,
                'data': request.form.to_dict()  # Save form data
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        session['user_id'] = 'example_user_id'  # Set user ID after successful login
        return redirect(url_for('handle_post_request'))  # Redirect to handle original request
    return '<form method="post">Login form</form>'

@app.route('/handle_post_request', methods=['POST'])
@login_required
def handle_post_request():
    if 'original_request' in session:
        original_request = session.pop('original_request')

        # Execute the original POST request
        # Here you can process the original request data
        # Example: return original data as JSON response
        return {'message': 'Original POST executed', 'data': original_request['data']}

    return 'Unhandled POST request', 400

@app.route('/some_protected_route', methods=['POST'])
@login_required
def some_protected_route():
    return 'Success! You are authenticated.'

if __name__ == '__main__':
    app.run(debug=True)
