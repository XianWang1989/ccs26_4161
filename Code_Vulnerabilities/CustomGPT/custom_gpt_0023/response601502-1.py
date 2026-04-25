
from flask import Flask, session, redirect, url_for, request, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# A decorator to check if the user is logged in
def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the original request for after logging in
            session['original_request'] = {
                'url': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authentication logic here (e.g., check username and password)
        session['logged_in'] = True
        return redirect(url_for('handle_post'))
    return 'Login Page'

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post():
    # Process your POST request
    return 'POST request executed successfully!'

@app.route('/execute_after_login', methods=['POST'])
def execute_after_login():
    if 'original_request' in session:
        original_request = session.pop('original_request')
        # Redirecting to the original path
        return redirect(original_request['url'], code=303)

# Example POST endpoint that requires login
@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # Handle the POST request here
    return 'Form submitted!', 200

if __name__ == '__main__':
    app.run(debug=True)
