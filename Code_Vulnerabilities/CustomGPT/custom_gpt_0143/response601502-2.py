
@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    data = request.form
    return "Data processed: " + str(data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['logged_in'] = True

        # Re-execute the original POST request using Flask's test_client
        if 'next_url' in session and session['request_method'] == 'POST':
            with app.test_request_context(path=session['next_url'], method='POST', data=session['request_data']):
                return post_endpoint()

        return redirect(url_for('home'))
    return "Login Page"
