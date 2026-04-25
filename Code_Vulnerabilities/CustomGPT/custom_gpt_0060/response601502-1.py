
from flask import Flask, session, redirect, url_for, request, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate user authentication
        username = request.form['username']
        password = request.form['password']
        if username == 'user' and password == 'pass':  # Replace with real authentication
            session['logged_in'] = True
            flash('Login successful!')

            # After login, check if there is a stored POST request to process
            original_request = session.pop('original_request', None)
            if original_request:
                return redirect(original_request['path'], code=303)

            return redirect(url_for('home'))

        flash('Invalid credentials, please try again.')

    return '''
        <form method="post">
            Username: <input type="text" name="username">
            Password: <input type="password" name="password">
            <input type="submit">
        </form>
    '''

@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    if not session.get('logged_in'):
        # Store the original request information in the session
        session['original_request'] = {
            'path': request.path,
            'data': request.form.to_dict()
        }
        return redirect(url_for('login'))

    # Handle the POST request normally
    data = request.form
    return jsonify({"message": "Post request successful!", "data": data})

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
