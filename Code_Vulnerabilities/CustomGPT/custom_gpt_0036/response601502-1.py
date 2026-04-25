
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store the original request method and form data in the session
            session['original_request'] = {
                'url': request.path,
                'form_data': request.form.to_dict()  # Convert ImmutableMultiDict to a normal dict
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic...
        session['logged_in'] = True
        flash('Logged in successfully.')

        # Check if there's an original request in session
        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(original_request['url'], code=303)  # Perform a POST-Redirect-GET

    return render_template('login.html')

@app.route('/post_view', methods=['POST'])
@login_required
def post_view():
    # Handle the POST request here
    data = request.form
    # Process the data...
    return 'Data processed: {}'.format(data)

if __name__ == '__main__':
    app.run(debug=True)
