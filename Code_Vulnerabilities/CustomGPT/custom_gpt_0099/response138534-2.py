
@app.route('/elastic_ips/<region>')
def view_elastic_ips(region):
    # Logic to fetch and render Elastic IPs for the region
    return render_template('elastic_ips.html', region=region, elastic_ips=elastic_ips)  # your template
