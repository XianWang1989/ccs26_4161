
@app.route('/elastic_ips/<region>')
def view_elastic_ips(region):
    # Logic to display the list of Elastic IPs for the given region
    # ...

    return render_template('elastic_ips.html', region=region, elastic_ips=elastic_ips)
