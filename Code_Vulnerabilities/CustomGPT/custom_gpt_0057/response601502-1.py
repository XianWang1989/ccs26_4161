
from flask import Flask, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['post_data'] = {
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform your login logic here
        session['logged_in'] = True
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(post_data['path'], code=303)
        return redirect(url_for('home'))
    return 'Login Page - Please log in'

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle your original POST request here
    return jsonify(success=True, data=request.form)

@app.route('/home')
def home():
    return 'Welcome Home!'

if __name__ == '__main__':
    app.run(debug=True)
