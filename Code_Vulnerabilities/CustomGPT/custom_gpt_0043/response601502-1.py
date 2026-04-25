
from flask import Flask, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Set an appropriate secret key

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original POST request body in the session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        user_id = request.form.get('user_id')  # Example login logic
        session['user_id'] = user_id

        # Check if there is stored POST data to process
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(url_for('handle_post', **post_data))

        return redirect(url_for('home'))

    return 'Login Form'

@app.route('/handle_post', methods=['POST'])
def handle_post():
    # Example of handling the original POST
    data = request.form
    return jsonify({"message": "POST handled successfully!", "data": data})

@app.route('/protected_post', methods=['POST'])
@login_required
def protected_post():
    return jsonify({"status": "This is a protected POST endpoint."})

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
