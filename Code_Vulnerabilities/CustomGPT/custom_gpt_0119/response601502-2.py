
@app.route('/protected', methods=['POST'])
def protected():
    if not session.get('logged_in'):
        # Store the original request path and form data
        session['original_path'] = request.path
        session['original_form'] = request.form.to_dict()
        return redirect(url_for('login'))
    return 'Success!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['logged_in'] = True
        # After logging in, check if we have an original request
        if 'original_path' in session:
            return redirect(url_for('replay_protected_request'))
    return render_template('login.html')

@app.route('/replay_protected_request', methods=['POST'])
def replay_protected_request():
    form_data = session.pop('original_form', {})
    # Process the original POST request
    return f"Replaying original request with data: {form_data}"

if __name__ == '__main__':
    app.run()
