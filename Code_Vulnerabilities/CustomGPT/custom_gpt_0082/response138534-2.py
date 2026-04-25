
@app.route('/elastic_ips/<region>')
def elastic_ips(region):
    # Your logic to display the elastic IPs
    return render_template('elastic_ips.html', region=region)
