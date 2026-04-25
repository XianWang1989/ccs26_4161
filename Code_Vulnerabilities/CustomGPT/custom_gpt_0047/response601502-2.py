
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        if 'original_request' in session:
            func_name, params = session.pop('original_request')
            return globals()[func_name](**params)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/original-post', methods=['POST'])
@login_required
def original_post_request_handler():
    return "Original POST request processed!"

def handle_post_request():
    func_name = 'original_post_request_handler'
    params = request.form.to_dict()
    session['original_request'] = (func_name, params)
    return redirect(url_for('login'))

@app.route('/post-handler', methods=['POST'])
def post_handler():
    return handle_post_request()

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
