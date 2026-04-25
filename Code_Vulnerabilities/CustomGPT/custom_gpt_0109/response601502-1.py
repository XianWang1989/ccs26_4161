
from flask import Flask, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def is_logged_in():
    return 'user' in session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user login logic here
        session['user'] = request.form['username']
        # After logging in, check for any pending requests
        if 'post_data' in session:
            post_data = session['post_data']
            # Clear the session data
            del session['post_data']
            return handle_post_request(post_data['path'], post_data['data'])
        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/protected', methods=['POST'])
def protected():
    if not is_logged_in():
        # Store the original POST data in session
        session['post_data'] = {
            'path': request.path,
            'data': request.form.to_dict()  # Convert form data to a dictionary
        }
        return redirect(url_for('login'))

    return handle_post_request(request.path, request.form)

def handle_post_request(path, data):
    # Here you would process the original POST request
    # For demonstration, we will just return the data
    return jsonify({"message": "Success", "data": data})

@app.route('/home')
def home():
    return 'Welcome Home'

if __name__ == '__main__':
    app.run(debug=True)
