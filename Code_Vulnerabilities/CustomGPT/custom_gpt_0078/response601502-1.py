
from flask import Flask, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function for user login
def login(username, password):
    # Authenticate user (this is just a placeholder)
    return True

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if login(username, password):  # Simulate user login
            # Check if there's a pending request in session
            if 'pending_request' in session:
                original_request = session.pop('pending_request')
                return handle_post_request(original_request['url'], original_request['data'])
            return redirect(url_for('home'))

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/protected-endpoint', methods=['POST'])
def protected_endpoint():
    if not session.get('logged_in'):
        # Store the original request data
        session['pending_request'] = {
            'url': request.path,
            'data': request.form.to_dict()
        }
        return redirect(url_for('login'))

    # Handle the POST request here
    return jsonify({"message": "Request successful!", "data": request.form})

def handle_post_request(url, data):
    with app.test_request_context(url, method='POST', data=data):
        response = protected_endpoint()  # Call the protected endpoint
        return response

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
