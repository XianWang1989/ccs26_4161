
from flask import Flask, session, redirect, url_for, request
from flask import flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request if user is not logged in
            session['original_request'] = {
                'url': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic...
        session['user_id'] = 'some_user_id'  # Simulate a successful login
        flash('Login successful!')

        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(original_request['url'], code=303)  # See Other

    return '<form method="POST">Login Form</form>'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Process the original post request
    data = request.form
    return f"Data received: {data}"

if __name__ == '__main__':
    app.run(debug=True)
