
from flask import Flask, request, redirect, session, url_for, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the POST data in session
            session['next_url'] = request.url
            session['post_data'] = request.form.to_dict()  # Store form data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        session['user_id'] = 'authenticated_user'  # Replace with actual user identification
        return redirect(session.get('next_url', '/'))  # Redirect to the original page

    return render_template('login.html')  # Your login template

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # This is your protected POST endpoint
    data = request.form
    return f'Post data received: {data}', 200

@app.route('/retry_post', methods=['POST'])
def retry_post():
    if 'post_data' in session:
        # Re-execute the original request with stored data
        response = app.test_client().post(session['next_url'], data=session['post_data'])
        session.pop('post_data', None)  # Clear stored data
        return response
    return 'No stored data', 400

if __name__ == '__main__':
    app.run()
