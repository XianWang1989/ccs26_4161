
from flask import Flask, request, session, redirect, url_for, jsonify, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the request data before redirecting to login
            session['next_request'] = {
                'method': request.method,
                'url': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login logic here
        session['user_id'] = 'some_user_id'  # Assuming user ID is set after successful login

        # Check if there was a stored request to process after login
        next_request = session.pop('next_request', None)
        if next_request:
            return redirect(next_request['url'], code=303)  # Use 303 to redirect for POST
    return render_template('login.html')

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request
    data = request.form
    # Process data
    return jsonify({"message": "Success", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
