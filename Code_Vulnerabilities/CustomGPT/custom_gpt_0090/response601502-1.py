
from flask import Flask, request, redirect, session, url_for, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy login function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request method and data
            session['post_url'] = request.path
            session['post_data'] = request.form.to_dict()  # Store form data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['user_id'] = 'some_user_id'  # Set user session

        # Check if there was a stored POST request
        if 'post_url' in session and 'post_data' in session:
            post_url = session.pop('post_url')
            post_data = session.pop('post_data')
            return redirect(post_url)  # Redirect to the original post

    return render_template('login.html')  # Render login page

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # Handle the original POST request after the user is logged in
    data = request.form
    # Process your data here
    return 'Data processed: {}'.format(data)

if __name__ == '__main__':
    app.run(debug=True)
