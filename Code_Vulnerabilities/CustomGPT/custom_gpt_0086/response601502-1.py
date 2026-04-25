
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['POST'])
def login():
    # Handle user login
    # If successful:
    next_url = session.pop('next_url', None)
    post_data = session.pop('post_data', None)

    if post_data:
        # Re-execute original POST request
        return handle_protected_post(post_data)

    return redirect(next_url or '/')

@app.route('/protected', methods=['POST'])
def protected():
    if not session.get('logged_in'):
        session['next_url'] = request.full_path
        session['post_data'] = request.form  # Store form data
        return redirect(url_for('login'))

    return handle_protected_post(request.form)

def handle_protected_post(data):
    # Process the data from the original POST request
    # Example processing
    return f"Data processed: {data}"

if __name__ == '__main__':
    app.run()
