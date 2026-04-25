
@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to retrieve and display elastic IPs
    return render_template('elastic_ips.html', region=region, elis=elastic_ips)
