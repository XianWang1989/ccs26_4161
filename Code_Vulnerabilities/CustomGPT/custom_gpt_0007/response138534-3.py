
@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Your logic to retrieve and display Elastic IPs goes here.
    return render_template('list_elastic_ips.html', region=region)
