
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data in session
            session['original_post'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user_id'] = 1  # Example user ID
        original_post = session.pop('original_post', None)

        if original_post:
            # Resend the original POST request data
            return redirect(url_for('handle_post', **original_post))

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/post-endpoint', methods=['POST'])
@login_required
def handle_post():
    # Access the original POST data
    data = request.form
    # Process the data here
    return 'Data processed: ' + str(data)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

if __name__ == '__main__':
    app.run(debug=True)
