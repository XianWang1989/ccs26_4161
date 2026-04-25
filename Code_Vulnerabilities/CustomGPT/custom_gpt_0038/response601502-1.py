
from flask import Flask, request, redirect, session, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy authentication check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            session['original_post'] = (request.path, request.form.to_dict())
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user authentication is successful
        session['logged_in'] = True
        flash('Logged in successfully.')
        # After login, check for saved POST data
        if 'original_post' in session:
            path, form_data = session.pop('original_post')
            return redirect(path)  # Redirect to the original path
    return render_template('login.html')

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_handler():
    data = request.form
    # Process the data as required
    return 'Post request processed!'

if __name__ == '__main__':
    app.run(debug=True)
