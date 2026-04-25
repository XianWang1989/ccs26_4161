
from flask import Flask, request, redirect, session, url_for, render_template
from flask_login import LoginManager, login_user, login_required, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    # Load user from your user model
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        user = authenticate(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            # After login, check for stored request
            if 'post_request' in session:
                # Execute stored POST request
                return execute_stored_post(session.pop('post_request'))
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Your protected logic here
    return 'This is a protected resource.'

def store_post_request():
    data = request.form.to_dict()
    session['post_request'] = {
        'endpoint': request.url,
        'data': data
    }
    return redirect(url_for('login'))

def execute_stored_post(stored_request):
    with app.test_request_context(stored_request['endpoint'], method='POST', data=stored_request['data']):
        response = app.full_dispatch_request()
        return response

@app.before_request
def login_protected():
    if request.method == 'POST' and not current_user.is_authenticated:
        return store_post_request()

if __name__ == '__main__':
    app.run(debug=True)
