
from flask import Flask, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for user authentication goes here.
        # If successful:
        session['user_id'] = 'user_id'  # Set user_id in session

        # Check if there's a stored post request
        if 'post_data' in session:
            post_data = session['post_data']
            # Redirect to the POST route with the stored POST data
            return redirect(url_for(post_data['endpoint'], **post_data['params']))  # Your logic to handle the endpoint

    return 'Login Page'

@app.route('/protected_post', methods=['POST'])
def protected_post():
    if 'user_id' not in session:
        # Store POST data in session and redirect to login
        session['post_data'] = {
            'endpoint': 'protected_post',
            'params': request.form.to_dict(),  # Convert form data to dict
        }
        return redirect(url_for('login'))

    # Handle the POST request normally
    return 'Protected POST request processed successfully!'
