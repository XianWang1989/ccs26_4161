
from flask import Flask, request, redirect, session, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # necessary for session management

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming authentication logic
        # On successful login:
        session['logged_in'] = True
        flash('Logged in successfully.')

        # Check if there's a stored POST request
        if 'post_data' in session:
            return redirect(session['post_data']['url'], code=303)  # Use 303 to indicate a post-redirect


@app.route('/protected', methods=['POST'])
def protected():
    if not session.get('logged_in'):
        # Store the request data
        session['post_data'] = {
            'url': request.path,
            'form_data': request.form.to_dict()  # Store the form data as a dictionary
        }
        return redirect(url_for('login'))

    # Handle the POST request normally
    return 'Protected POST request successful!'

@app.route('/execute_post', methods=['POST'])
def execute_post():
    # Optionally handle any post requests explicitly
    # This can be linked as a callback to the original post operation
    return 'Executing the original data with: {}'.format(request.form)

if __name__ == '__main__':
    app.run(debug=True)
