
@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to retrieve and display elastic IPs for the specified region
    return render_template('list_elastic_ips.html', region=region)
