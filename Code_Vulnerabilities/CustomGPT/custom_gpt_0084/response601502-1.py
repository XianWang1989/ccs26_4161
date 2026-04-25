
from flask import Flask, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume login logic here
        session['user'] = 'authenticated_user'
        # Check for a stored post request
        if 'post_action' in session:
            post_action = session.pop('post_action')
            return redirect(post_action['url'], code=303)
        return redirect(url_for('home'))
    return 'Login Form'

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    return 'Protected POST request executed!'

@app.route('/protected_action', methods=['POST'])
def protected_action():
    if 'user' not in session:
        # Store the intended action and return to login
        session['post_action'] = {
            'url': url_for('protected'),
            'data': request.form.to_dict()
        }
        flash('Please log in to continue.')
        return redirect(url_for('login'))

    # Process the request normally if logged in
    return protected()

if __name__ == '__main__':
    app.run()
