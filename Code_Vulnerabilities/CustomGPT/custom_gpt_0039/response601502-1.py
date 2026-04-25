
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            session['post_request_data'] = {
                'path': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['logged_in'] = True
        flash('Logged in successfully!')

        # Check if there was a POST request saved in the session
        if 'post_request_data' in session:
            path = session['post_request_data']['path']
            form_data = session['post_request_data']['form_data']

            # Clear the stored data
            del session['post_request_data']

            # Re-create the POST request to the original path
            with app.test_request_context(path, method='POST', data=form_data):
                return handle_post_request()

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def handle_post_request():
    # Handle the original POST request
    data = request.form
    # Process the data as needed
    return 'POST request processed: {}'.format(data)

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
