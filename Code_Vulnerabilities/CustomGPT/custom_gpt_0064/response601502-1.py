
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            # Store original request details
            session['original_post'] = {
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user'] = request.form['username']
        flash('Logged in successfully!')

        # Check for original POST request
        if 'original_post' in session:
            original_post = session.pop('original_post')
            return handle_post_request(original_post['data'], original_post['path'])

        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/some_post_endpoint', methods=['POST'])
@login_required
def some_post_endpoint():
    # Handle the initial POST request
    return "Handled POST request!"

def handle_post_request(form_data, path):
    # You can use Flask's test client to simulate a POST request or directly handle the data
    with app.test_request_context(path, method='POST', data=form_data):
        return some_post_endpoint()

@app.route('/')
def index():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
