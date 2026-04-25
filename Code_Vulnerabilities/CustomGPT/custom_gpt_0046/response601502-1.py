
from flask import Flask, request, redirect, session, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            # Store original request info
            session['original_request'] = {
                'method': request.method,
                'url': request.url,
                'data': request.form.to_dict(),
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume login logic here sets session['logged_in'] = True
        session['logged_in'] = True
        original_request = session.pop('original_request', None)

        if original_request:
            # Re-execute the original POST request
            return app.view_functions[original_request['url']](**original_request['data'])

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the post request
    return f"Received: {request.form}"

@app.route('/')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
