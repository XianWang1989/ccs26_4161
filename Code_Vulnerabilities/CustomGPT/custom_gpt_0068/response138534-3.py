
@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to display the list of Elastic IPs
    # Render a template that shows the IPs
    return render_template('elastic_ips.html', region=region)
