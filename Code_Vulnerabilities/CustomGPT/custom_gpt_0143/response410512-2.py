
@app.route('/generate-file', methods=['GET'])
def generate_file():
    filename = 'dynamic_file.png'
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Code to generate the file goes here

    return f'http://your_domain.com/media/{filename}'
