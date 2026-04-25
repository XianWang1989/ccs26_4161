
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume login logic here...
        session['user'] = 'username'  # Example user after login
        flash('Logged in successfully!')
        return redirect(url_for('handle_post_after_login'))
    return render_template('login.html')

@app.route('/secure-post', methods=['POST'])
def secure_post():
    if 'user' not in session:
        # Store POST data in session
        session['post_data'] = request.form.to_dict()  # Store form data
        return redirect(url_for('login'))  # Redirect to login
    else:
        # Process the POST request normally
        data = request.form
        # (Handle your data here)
        return 'Post processed with data: ' + str(data)

@app.route('/handle_post_after_login')
def handle_post_after_login():
    # After login, check for stored post data
    post_data = session.pop('post_data', None)
    if post_data:
        # Simulate processing of the POST request
        return 'Post executed with saved data: ' + str(post_data)
    return 'No post data to process.'

if __name__ == '__main__':
    app.run(debug=True)
