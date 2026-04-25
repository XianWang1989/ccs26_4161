
@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Release the Elastic IP
    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Redirect back to the region page (you may need to adjust the URL)
    return redirect(url_for('your_region_page', region=region))

@app.route('/elastic_ips/<region>')
def your_region_page(region):
    # Logic to render the page for the region
    return render_template('your_region_template.html', region=region)
