
@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    if 'logged_in' not in session:
        session['post_data'] = request.form.to_dict()  # Store form data
        return redirect(url_for('login')) 

    # If the user was already logged in, process the form data
    data = session.pop('post_data', request.form)  # Retrieve and clear the stored POST data if available
    # Handle the data as needed
    return "Post Successful", 200
