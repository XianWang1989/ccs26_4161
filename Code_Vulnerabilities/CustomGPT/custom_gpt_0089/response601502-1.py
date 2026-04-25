
from flask import Flask, request, redirect, session, url_for, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user authentication is successful
        session['user'] = 'authenticated_user'

        # After login, check if there's stored post data
        if 'request_data' in session:
            endpoint = session['request_data']['endpoint']
            data = session['request_data']['data']
            del session['request_data']  # Clear after use
            return redirect(url_for(endpoint, **data))  # Use GET to redirect, or directly handle the POST if needed

    return render_template('login.html')  # Render your login template here

# Protected POST route
@app.route('/protected', methods=['POST'])
def protected():
    if 'user' not in session:
        session['request_data'] = {'endpoint': 'protected', 'data': request.form}
        return redirect(url_for('login'))  # Redirect to login if not authenticated

    # Handle the POST request as normal
    return jsonify({"message": "This is a protected response!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
