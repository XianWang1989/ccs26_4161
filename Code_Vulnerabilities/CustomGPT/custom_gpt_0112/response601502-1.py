
from flask import Flask, request, session, redirect, url_for, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    # Your login required decorator implementation here
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle user login
    if request.method == 'POST':
        # Perform login logic
        session['logged_in'] = True
        next_route = session.pop('next_post', None)
        if next_route:
            return redirect(next_route)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected-post', methods=['POST'])
@login_required
def protected_post():
    if not session.get('logged_in'):
        session['next_post'] = request.path
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))

    # Handle the original POST request
    return jsonify({"message": "Success", "data": request.form})

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

if __name__ == "__main__":
    app.run(debug=True)
