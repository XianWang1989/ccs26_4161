
from flask import Flask, request, session, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['next_func'] = f.__name__
            session['next_args'] = request.form.to_dict()  # Store POST parameters
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = 'user_id_here'  # Authenticate user
        func_name = session.pop('next_func', None)
        params = session.pop('next_args', {})
        if func_name:
            return globals()[func_name](**params)  # Execute function with parameters
        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    data = request.form['data']
    # Process the data here
    return 'Data submitted: ' + data

if __name__ == '__main__':
    app.run(debug=True)
