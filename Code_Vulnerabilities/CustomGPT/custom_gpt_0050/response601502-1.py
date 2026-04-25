
from flask import Flask, request, session, redirect, url_for, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Save the original request data
            session['original_url'] = request.url
            session['original_method'] = request.method
            session['original_data'] = request.form.to_dict()  # Capture POST data
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login (check credentials)
        session['user_id'] = 'authenticated_user'  # Mock authentication
        return redirect(session.pop('original_url', url_for('home')))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the original POST request
    return jsonify({"message": "This is a protected resource.", "data": request.form})

@app.route('/')
def home():
    return 'Welcome to Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
