
from flask import Flask, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            # Store original request path and data
            session['original_request'] = {
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['user_id'] = 'authenticated_user'  # Example user
        # After login, check if there's an original request
        if 'original_request' in session:
            original_request = session.pop('original_request')
            return redirect(original_request['path'])
    return 'Login Page'  # Render your login page here

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # This function will only be reached if the user is authenticated
    # Process the submitted data
    data = request.form
    return f"Data submitted: {data}"

if __name__ == "__main__":
    app.run(debug=True)
