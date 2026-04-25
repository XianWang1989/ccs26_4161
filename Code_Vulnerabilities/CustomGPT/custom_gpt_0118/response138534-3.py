
@app.route('/elastic_ips/<region>')
def your_redirect_route(region):
    # Logic to display the elastic IPs or relevant information
    return render_template('your_template.html', region=region)
