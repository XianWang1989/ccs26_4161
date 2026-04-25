
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/protected', methods=['POST'])
def protected():
    if not session.get('logged_in'):
        # Store the original request data in the session
        session['request_data'] = {
            'method': request.method,
            'form': request.form.to_dict()
        }
        return redirect(url_for('login'))  # Redirect to login page
    # Handle the POST request here
    return 'Success!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['logged_in'] = True
        # After logging in, check if there's stored request data
        if 'request_data' in session:
            return replay_request()
    return render_template('login.html')

def replay_request():
    data = session.pop('request_data', {})
    if data.get('method') == 'POST':
        # Process the original POST request using the form data
        return f"Replaying request with data: {data['form']}"
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return 'Welcome to the index page.'

if __name__ == '__main__':
    app.run()
