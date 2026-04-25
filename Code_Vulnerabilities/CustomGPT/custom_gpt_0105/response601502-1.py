
from flask import Flask, request, redirect, session, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated users for login
users = {'user': 'password'}

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            # Store request data before redirect
            session['next_url'] = request.url
            session['form_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username

            # After login, check if there's a next_url to redirect
            next_url = session.pop('next_url', None)
            form_data = session.pop('form_data', None)
            if next_url and form_data:
                return redirect(next_url)
            return redirect(url_for('home'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/post-data', methods=['POST'])
@login_required
def post_data():
    # Process the POST request
    data = request.form['data']
    return f"Data received: {data}"

@app.route('/')
def home():
    return 'Welcome to the home page! Please log in to post data.'

if __name__ == '__main__':
    app.run(debug=True)
