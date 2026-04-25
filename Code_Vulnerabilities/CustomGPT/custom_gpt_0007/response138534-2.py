
@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []

    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optionally flash a message to the user
    flash('Elastic IP deleted successfully!')

    # Redirect to a specified route after deletion, for instance, back to the list of Elastic IPs
    return redirect(url_for('list_elastic_ips', region=region))
