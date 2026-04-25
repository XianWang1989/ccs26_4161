
from flask import Flask, redirect, url_for, session, request, jsonify, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the request method and data
            session['requested_url'] = request.url
            session['request_method'] = request.method
            session['form_data'] = request.form.to_dict()  # Store form data if POST
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authentication logic here
        session['logged_in'] = True
        flash('You were logged in')

        # Check if there's a requested URL to redirect to
        if 'requested_url' in session:
            requested_url = session.pop('requested_url')
            method = session.pop('request_method')
            form_data = session.pop('form_data', None)

            if method == 'POST' and form_data:
                # Simulate a POST request by calling the route directly
                with app.test_request_context(requested_url, method='POST', data=form_data):
                    return handle_post()
            return redirect(requested_url)  # Redirect for GET requests

    return 'Login Form'

@app.route('/protected', methods=['POST'])
@login_required
def handle_post():
    # Handle your POST request
    return jsonify(success=True, message='POST request processed.')

if __name__ == '__main__':
    app.run(debug=True)
