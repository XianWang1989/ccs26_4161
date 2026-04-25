
@app.route('/generate-file', methods=['GET'])
def generate_file():
    # Generate dynamic content
    content = "This is some dynamically generated content."

    # Create a temporary file
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    with open(temp.name, 'w') as f:
        f.write(content)

    # Return the URL where the file can be accessed
    return jsonify({'file_url': f'http://your_server_domain_or_ip/files/{os.path.basename(temp.name)}'})
