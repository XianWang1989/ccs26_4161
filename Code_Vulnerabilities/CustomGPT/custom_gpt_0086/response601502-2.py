
from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['POST'])
def login():
    # Handle login logic
    original_func = session.pop('original_func', None)
    form_data = session.pop('form_data', None)

    if original_func and form_data:
        return original_func(**form_data)

    return redirect('/')

def require_login(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            session['original_func'] = f
            session['form_data'] = request.form.to_dict()  # Store form data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/protected', methods=['POST'])
@require_login
def protected():
    # Process the data from the POST request
    return f"Protected data processed: {request.form}"

if __name__ == '__main__':
    app.run()
