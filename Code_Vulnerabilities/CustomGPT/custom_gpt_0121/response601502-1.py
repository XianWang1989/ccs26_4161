
from flask import Flask, request, redirect, session, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication
def is_authenticated():
    return session.get('logged_in', False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming authentication is successful
        session['logged_in'] = True
        return redirect(session.get('next_url', url_for('home')))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
def protected():
    if not is_authenticated():
        # Store the next URL and the form data in session
        session['next_url'] = request.path
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))

    # Handle the POST request normally if authenticated
    return jsonify({'message': 'This is a protected post!', 'data': request.form}), 200

@app.route('/handle_post_login', methods=['POST'])
def handle_post_login():
    if is_authenticated():
        # Retrieve and execute the original POST request
        post_data = session.pop('post_data', None)
        if post_data:
            # Process the stored POST request
            return jsonify({'message': 'Executed POST after login', 'data': post_data}), 200
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
