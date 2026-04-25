
from flask import Flask, session, redirect, request, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['original_request'] = {
                'method': request.method,
                'path': request.path,
                'form': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume login successful
        session['user_id'] = 'some_user_id'
        flash('Logged in successfully.')

        # Check if there's an original request to process
        if 'original_request' in session:
            original_request = session.pop('original_request')
            return handle_original_request(original_request)

        return redirect(url_for('home'))

    return render_template('login.html')

def handle_original_request(original_request):
    if original_request['method'] == 'POST':
        # Directly call the function associated with the route, passing form data
        return post_handler(original_request['form'])
    return redirect(url_for('home'))  # Fallback for non-POST requests

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_handler():
    data = request.form
    # Process the data
    return "Data processed: {}".format(data)

@app.route('/home')
def home():
    return "Welcome to Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
