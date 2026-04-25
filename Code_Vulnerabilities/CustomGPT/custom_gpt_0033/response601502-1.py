
from flask import Flask, request, redirect, url_for, session, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data
            session['original_post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate login credentials (this part is simplified)
        session['user_id'] = 'example_user'

        # Check if there's original POST data to process
        original_data = session.pop('original_post_data', None)
        if original_data:
            # Re-execute the original POST request
            return redirect(url_for('protected_post', **original_data))

        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected_post():
    # Handle the POST request
    data = request.form
    return jsonify({'message': 'Handled POST request successfully!', 'data': data})

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
