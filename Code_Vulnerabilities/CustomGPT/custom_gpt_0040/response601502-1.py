
from flask import Flask, request, redirect, url_for, session, render_template, flash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user authentication
def is_authenticated():
    return session.get('logged_in', False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Replace with actual user authentication
        if username == 'user' and check_password_hash('password_hash', password):
            session['logged_in'] = True
            # Check if there's a stored next request
            if 'next_post' in session:
                next_url = session.pop('next_post')
                return redirect(next_url)
            return redirect(url_for('home'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
def protected():
    if not is_authenticated():
        # Store the original request data in the session
        session['next_post'] = request.path
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))

    # Handle the POST request
    # For example: process the data here
    data = request.form
    return 'Protected POST request successful!'

@app.route('/process_post', methods=['POST'])
def process_post():
    if not is_authenticated():
        return redirect(url_for('login'))

    # Here you can directly process the POST request
    data = request.form
    return 'Processed post with data: {}'.format(data)

if __name__ == '__main__':
    app.run(debug=True)
