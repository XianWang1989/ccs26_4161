
from flask import Flask, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login required decorator
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data
            session['post_url'] = request.path
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user is authenticated
        session['user_id'] = 'some_user_id'

        # Check for stored POST request
        if 'post_url' in session and 'post_data' in session:
            post_url = session.pop('post_url')
            post_data = session.pop('post_data')
            return redirect(post_url, code=307)  # 307 preserves POST method

    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle your post request logic here
    data = request.form
    return f'Protected POST request received with data: {data}'

if __name__ == '__main__':
    app.run(debug=True)
