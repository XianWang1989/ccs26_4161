
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data
            session['original_request'] = {
                'method': request.method,
                'path': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming login is successful
        session['user_id'] = 'user_id_value'  # Example logged-in user ID
        original_request = session.pop('original_request', None)

        if original_request:
            # Reissue the original POST request
            if original_request['method'] == 'POST':
                return post_handler(original_request['form_data'])

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_handler():
    # Handle your POST request data
    data = request.form
    # Process the data...
    return 'Data processed successfully!'

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
