
from flask import Flask, request, redirect, session, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# Mock user store
users = {'user': 'password'}

@login_manager.user_loader
def load_user(username):
    return username if username in users else None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            login_user(username)
            # Check if there’s any original POST data to process
            if 'post_data' in session:
                post_data = session.pop('post_data')
                return redirect(url_for(post_data['endpoint'], **post_data['params']))
            return redirect(url_for('home'))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    return 'This is a protected POST request'

@app.route('/handle_post', methods=['POST'])
def handle_post():
    if not session.get('user_authenticated'):
        # Storing POST data in session
        session['post_data'] = {'endpoint': 'protected', 'params': request.form.to_dict()}
        # Redirecting to login
        return redirect(url_for('login'))
    return protected()

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
