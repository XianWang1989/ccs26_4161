
@app.route('/execute_original_post', methods=['POST'])
@login_required
def execute_original_post():
    endpoint = session.pop('next_endpoint', None)
    post_data = session.pop('post_data', {})

    if endpoint:
        # Call the relevant function here
        return app.view_functions[endpoint](**post_data)

    return 'No original POST action available.'
