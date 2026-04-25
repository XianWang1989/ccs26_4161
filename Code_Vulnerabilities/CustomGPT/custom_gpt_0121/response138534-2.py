
@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # logic to list elastic IPs for the region
    return render_template('your_template.html', region=region, elastic_ips=elastic_ips)
