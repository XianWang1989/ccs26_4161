
from flask import Flask, session, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
login_manager = LoginManager(app)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Logic to load a user from your data store goes here
    return User.get(user_id)  # Replace with your user loading logic

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user here
        # Assuming user is authenticated:
        user = User.authenticate(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            flash('Login successful!')

            # Check if there is pending POST data
            if 'post_data' in session:
                post_data = session.pop('post_data')  # Retrieve and remove stored POST data
                return handle_original_post(post_data)  # Call your function to handle original POST

            return redirect(url_for('home'))  # Redirect to a safe location if no pending request
    return render_template('login.html')

@app.route('/protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    # If user is not logged in, redirect to login
    if not session.get('user_logged_in'):
        # Store original request data in session
        session['post_data'] = request.form  # You can also use request.json if the data is JSON
        return redirect(url_for('login'))

    # Handle your regular POST request here
    process_data(request.form)
    return 'Success'

def handle_original_post(post_data):
    # Here you can reprocess the original POST request
    # For example, processing the form data as intended
    process_data(post_data)
    return 'Processed original POST after login!'

def process_data(data):
    # Your logic to handle the data goes here
    print('Processing data:', data)

@app.route('/')
def home():
    return 'Welcome to the Home Page'

if __name__ == '__main__':
    app.run(debug=True)
