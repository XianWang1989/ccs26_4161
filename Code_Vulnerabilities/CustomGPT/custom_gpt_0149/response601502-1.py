
from flask import Flask, request, redirect, url_for, session, render_template, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authentication logic here
        session['user_id'] = 'authenticated_user'
        post_data = session.pop('post_data', None)
        if post_data:
            # Redirect to the original endpoint with POST data
            return redirect(url_for(post_data['redirect_route'], **post_data))
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    data = request.form.to_dict()
    # Process the data
    return jsonify(success=True, data=data)

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
