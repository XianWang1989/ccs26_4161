from flask import Flask, request, redirect, url_for, session, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

# Dummy user data for login validation
USER_CREDENTIALS = {'username': 'test', 'password': 'password'}

# A decorator to simulate login_required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Route to simulate login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            next_url = request.args.get('next')
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home'))
        return 'Invalid credentials', 401
    return render_template('login.html')  # Simple login form

# Home route (just to show after login)
@app.route('/')
@login_required
def home():
    return 'Welcome to the home page!'

# Protected POST request
@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # Handle the original POST request here
    data = request.form.get('data')
    print(f"Processing data: {data}")
    return f"Data processed: {data}"

# Redirect user to login if POST request is made without being logged in
@app.route('/post-data', methods=['POST'])
def post_data():
    if 'user' not in session:
        # Store the form data in session before redirecting
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login', next=url_for('post_data')))
    
    # Process POST data once the user is logged in
    return submit()

if __name__ == '__main__':
    app.run(debug=True)
