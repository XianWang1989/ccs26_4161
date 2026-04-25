
@app.route('/protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    # Handle the POST request here
    return 'Original POST request executed!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate logging the user in
        session['logged_in'] = True
        return redirect(url_for('protected_endpoint'))  # Redirecting to the endpoint
    return 'Login Page'
