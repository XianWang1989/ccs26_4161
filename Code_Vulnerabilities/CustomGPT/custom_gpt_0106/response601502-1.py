
from flask import Flask, session, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user loader
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle user login
    if request.method == 'POST':
        # Assume user authentication logic here
        user = authenticate(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            post_data = session.pop('post_data', None)
            if post_data:
                return redirect(post_data['path'], code=303)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected-route', methods=['POST'])
@login_required
def protected_route():
    # Your protected logic here
    return 'Success!'

@app.before_request
def handle_login_redirect():
    if request.method == 'POST' and not current_user.is_authenticated:
        # Store the POST data in session
        session['post_data'] = {
            'path': request.path,
            'form_data': request.form.to_dict()
        }
        return redirect(url_for('login'))

@app.route('/execute-post', methods=['POST'])
@login_required
def execute_post():
    # Fetch stored data
    post_data = session.get('post_data')
    if post_data and request.path == post_data['path']:
        # Re-execute the post request with stored data
        return protected_route()  # Call the actual route

    return 'No valid post data found.'

if __name__ == '__main__':
    app.run(debug=True)
