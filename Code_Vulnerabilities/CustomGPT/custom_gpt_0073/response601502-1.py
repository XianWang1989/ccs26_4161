
from flask import Flask, request, session, redirect, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original POST data
            if request.method == 'POST':
                session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here and set session['user_id']
        session['user_id'] = 'some_user_id'
        flash('Logged in successfully!')

        # Check if there is post data to process
        if 'post_data' in session:
            post_data = session.pop('post_data')  # Remove from session
            return handle_post_request(post_data)

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the original post request
    data = request.form
    return f"Data processed: {data}"

def handle_post_request(data):
    # Here you'd typically call your original handler or process the data
    return f"Handled data after login: {data}"

@app.route('/')
def home():
    return 'Home page'

if __name__ == '__main__':
    app.run(debug=True)
